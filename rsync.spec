Name: rsync
Version: 2.6.9
Release: 1ev
Summary: A (remote) synchronisation utility
URL: http://rsync.samba.org/
Group: Applications/System
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://rsync.samba.org/ftp/rsync/rsync-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, popt, libacl
Requires: openssh, popt, libacl

%description
rsync is a replacement for rcp (and scp) that has many more features. It uses
the "rsync algorithm" which provides a very fast method for remote files into
sync. It does this by sending just the differences in the files across the
link, without requiring that both sets of files are present at one of the ends
of the link beforehand.


%prep
%setup -q

# Patch with included patches 

patch -p1 -b < patches/acls.diff
./prepare-source


%build
%configure \
	--disable-debug \
	--enable-acl-support \
	--with-rsync-path=%{_bindir}/rsync \
	--with-rsyncd-conf=/etc/rsyncd.conf 
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

# Create etc directory and touch a ghost config file

mkdir -p ${RPM_BUILD_ROOT}/etc/initng/daemon
touch ${RPM_BUILD_ROOT}/etc/rsyncd.conf

# Install rsync service file

cat << EOF > ${RPM_BUILD_ROOT}/etc/initng/daemon/rsyncd.i
#!/sbin/itype

daemon daemon/rsyncd {
    need = system/bootmisc virtual/net;
    exec daemon = %{_bindir}/rsync --daemon --no-detach;
}
EOF


%post
if /sbin/ngc -s 2>&1 | /bin/grep 'daemon/rsyncd'
then
	/sbin/ngc -r daemon/rsyncd > /dev/null 2>&1
fi

%postun
if [ "$1" -eq 0 ]
then
	/sbin/ngc -d daemon/rsyncd > /dev/null 2>&1 || :
	/sbin/ng-update del daemon/rsyncd > /dev/null 2>&1 || :
fi


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc *NEWS README TODO COPYING 
/etc/initng/daemon/rsyncd.i
%ghost %config(noreplace) /etc/rsyncd.conf
%{_bindir}/rsync
%{_mandir}/man1/rsync.1.gz
%{_mandir}/man5/rsyncd.conf.5.gz
