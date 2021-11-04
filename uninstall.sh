if [ -e "/opt/ha/dist-packages/pyagent/disk_percent" ];then
    /usr/bin/rm -rf /opt/ha/dist-packages/pyagent/disk_percent
fi

if [ -e "/opt/ha/resource/resources/disk_percent" ];then
    /usr/bin/rm -rf /opt/ha/resource/resources/disk_percent
fi
