#!/bin/bash
###### Netconfig file creation


menu_initial () {
clear
echo "*****************************  Netconfig file creation  *********************************"
echo "                                                                                        "
echo "   Welcome to NetConfig File creation                                    "
echo "                                                                                        "
echo "                                                                                        "
echo "   What do you want to do?                                                              "
echo "   1 - Scan the mac address run netmap                                                  "
echo "   2 - <option2>                                                                        "
echo "                                                                                        "
echo "   0 - Abort                                                                            "
echo "                                                                                        "
echo "******************************************************************************************"
read choice_1
        case $choice_1 in
            "1") export dsp_ch_1="Mac Scan";;
            "2") export dsp_ch_1="option_2";;
            "0") exit;;
        esac
}

menu_mac () {
clear
echo "*****************************  Netconfig file creation 1/5 *******************************"
echo "                                           *                                             "
echo "   Specify the MAC address of device       *   Selection:                                "
echo "                                           *   Netmap  : $dsp_ch_1                       "
echo "   1 - Press 1 to start recording          *                                             "
echo "                                           *                                             "
echo "                                           *                                             "
echo "   0 - Abort                               *                                             "
echo "                                           *                                             "
echo "******************************************************************************************"
read choice_2
        case $choice_2 in
            "1")
            echo "Please enter the mac address of the device(s):"
            read mac
            ;;
        "0") exit;;
        esac
}

menu_management () {
clear
echo "*****************************  Netconfig file creation 2/5 *******************************"
echo "                                           *                                             "
echo "   Specify the management IP   :           *   Selection:                                "
echo "                                           *   Netmap  : $dsp_ch_1                       "
echo "   1 - Press 1 to start recording          *   MAC scan: 🗸 done                          "
echo "                                           *                                             "
echo "                                           *                                             "
echo "   0 - Abort                               *                                             "
echo "                                           *                                             "
echo "******************************************************************************************"
read choice_3
        case $choice_3 in
            "1")
            echo "Please enter the management IP address for the switch"
            read ip
            ;;
        "0") exit;;
        esac
}

menu_uplink () {
clear
echo "*****************************  Netconfig file creation  3/5 ******************************"
echo "                                           *                                             "
echo "   Specify the uplink port     :           *   Selection:                                "
echo "                                           *   Netmap  : $dsp_ch_1                       "
echo "   1 - Press 1 to start recording          *   MAC scan: 🗸 done                          "
echo "                                           *   Management IP: 🗸 done                     "
echo "                                           *                                             "
echo "   0 - Abort                               *                                             "
echo "                                           *                                             "
echo "******************************************************************************************"
read choice_4
        case $choice_4 in
            "1")
            echo "Please enter the uplink port in the right format (ie: Brocade 1/1/3)"
            read uplink
            export dsp_ch_2=$uplink
            ;;
        "0") exit;;
        esac
}

menu_apstart () {
clear
echo "*****************************  Netconfig file creation  4/5 ******************************"
echo "                                           *                                             "
echo "   Specify the AP start port   :           *   Selection:                                "
echo "                                           *   Netmap  : $dsp_ch_1                       "
echo "   1 - Press 1 to start recording          *   MAC scan: 🗸 done                          "
echo "                                           *   Management IP: 🗸 done                     "
echo "                                           *   Uplink port: $dsp_ch_2                    "
echo "   0 - Abort                               *                                             "
echo "                                           *                                             "
echo "******************************************************************************************"
read choice_5
        case $choice_5 in
            "1")
            echo "Please enter the port of the first AP"
            read apstart
            ;;
        "0") exit;;
        esac
}

menu_apend () {
clear
echo "*****************************  Netconfig file creation  5/5 ******************************"
echo "                                           *                                             "
echo "   Specify the AP end port   :             *   Selection:                                "
echo "                                           *   Netmap  : $dsp_ch_1                       "
echo "   1 - Press 1 to start recording          *   MAC scan: 🗸 done                          "
echo "                                           *   Management IP: 🗸 done                     "
echo "                                           *   Uplink port: $dsp_ch_2                    "
echo "   0 - Abort                               *   AP port: From $apstart to $apend          "
echo "                                           *                                             "
echo "******************************************************************************************"
read choice_6
        case $choice_6 in
            "1")
            echo "Please enter the port of the last AP"
            read apend
            ;;
        "0") exit;;
        esac
}

menu_end () {
clear
echo "*****************************  Netconfig file creation  5/5 ******************************"
echo "                                           *                                             "
echo "   Netmap creation finish       :           *   Selection:                                "
echo "                                           *   Netmap  : $dsp_ch_1                       "
echo "   1 - Press 1 to run the script           *   MAC scan: 🗸 done                          "
echo "                                           *   Management IP: 🗸 done                     "
echo "                                           *   Uplink port: $dsp_ch_2                    "
echo "   0 - Abort                               *   AP port: From $apstart to $apend          "
echo "                                           *                                             "
echo "******************************************************************************************"
read choice_7
        case $choice_7 in
            "1")
            printf "$mac\t$ip\t$uplink\t$apstart\t$apend\n" > config
            nmap_file='config'
            #cat config
            COUNTER=0
             while IFS=$'\t' read -ra line; do
             	MAC[$COUNTER]=${line[0]}
             	IP[$COUNTER]=${line[1]}
             	COUNTER=$((COUNTER+1))
             done < config
            

            for ((i=0;$i<$COUNTER;i++)); do
            	echo "MAC: ${MAC[$i]}"
            	echo "IP: ${IP[$i]}"
            	hwlookup=$(curl -sL https://hwaddress.com/?q=${MAC[$i]} | sed -nr "/Company/s%^.*>(.*)</a.*$%\1%p")
            	echo "lookup: $hwlookup"
            	case $hwlookup in
            		"HP"|"Hewlett Packard Enterprise")
					
					;;
					"Brocade Communications Systems, Inc.")
					echo "Brocade routine"

					;;
					*)
					print "not supported vendor"
					exit 1
				esac
            done

            #printf "=========================\nWorking with MAC: $mac\n"
            ;;

        "0") exit;;
        esac
}



menu_initial
menu_mac
menu_management
menu_uplink
menu_apstart
menu_apend
menu_end
