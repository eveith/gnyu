Name: util-linux
Version: 2.13 
Release: 2ev
Summary: A random colleciton of important linux utilities
URL: ftp://ftp.de.kernel.org/linux/utils/util-linux
Group: System Environment/Base
License: GPL/BSD
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://ftp.de.kernel.org/linux/utils/%{name}/%{name}-%{version}-pre7.tar.bz2
Patch0: util-linux-2.12r-msp_config.diff
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, libpam, sed, e2fsprogs, gettext
Requires: libpam, e2fsprogs

%description
A collection of very important linux utilities, such as:
adjtimex agetty arch blockdev cal cfdisk chkdupexe clear clock col
colcrt colrm column ctrlaltdel cytune ddate dmesg dnsdomainname
domainname elvtune fdformat fdisk fsck.cramfs fsck.minix getopt
getoptprog hexdump hostname hwclock ipcrm ipcs isosize jaztool line
logger look losetup mcookie mesg mkfs mkfs.bfs mkfs.cramfs
mkfs.minix mkswap more mount namei nisdomainname pg pivot_root ramsize raw
rdev readprofile rename renice reset rev rootflags script setfdprm
setserial setsid setterm sfdisk sln strings swapoff swapon tput
tunelp ul umount update vidmode wall whereis write ypdomainname ziptool



%prep
%setup -q -n %{name}-%{version}-pre7
%patch -P 0 -p1


%build
%configure
make %{_smp_mflags} \
	CC=%{_target_platform}-gcc \
	OPT="$RPM_OPT_FLAGS -fomit-frame-pointer"


%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"

make install \
	DESTDIR="$RPM_BUILD_ROOT" \
	MAN_DIR="%{_mandir}" \
	INFO_DIR="%{_infodir}"

rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

%find_lang util-linux


%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/ipc.info.gz %{_infodir}/dir

%postun
/sbin/ldconfig
/sbin/install-info --delete %{_infodir}/ipc.info.gz %{_infodir}/dir


%clean
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"


%files -f util-linux.lang
%defattr(-, root, root)
%doc
/bin/*
%config /etc/fdprm
/sbin/*
%{_bindir}/*
%{_sbindir}/*
%{_infodir}/ipc.info*
%{_mandir}/*/*
%{_datadir}/misc/getopt/
