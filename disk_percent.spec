Name: SkybilityHA-disk-percent
Version: 2
Release: 1
Requires: python >= 2.6
Summary: disk monitor for SkybilityHA
Group: Development/System
License: GPL

%description
This is a disk space monitor script by yangyingfa@skybility.com

%prep
#

%build

%install
mkdir -p $RPM_BUILD_ROOT/opt/ha/resource/resources/disk_percent/disk/
mkdir -p $RPM_BUILD_ROOT/opt/ha/dist-packages/pyagent/disk_percent
cp disk.py $RPM_BUILD_ROOT/opt/ha/dist-packages/pyagent/disk_percent
touch $RPM_BUILD_ROOT/opt/ha/dist-packages/pyagent/disk_percent/__init__.py
cp meta-data.xml $RPM_BUILD_ROOT/opt/ha/resource/resources/disk_percent/disk/
exit 0

%files
/opt/ha/*

%postun
if [ "$1" = "0" ];then
    /usr/bin/rm -rf /opt/ha/dist-packages/pyagent/disk_percent
    /usr/bin/rm -rf /opt/ha/resource/resources/disk_percent
fi

