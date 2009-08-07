Name: util-linux-ng
Version: 2.13.0.1 
Release: 2ev
Summary: A random colleciton of important linux utilities
URL: http://userweb.kernel.org/~kzak/util-linux-ng/
Group: System Environment/Base
License: GPL/BSD
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp.kernel.org:/pub/linux/utils/%{name}/v2.13/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make, gcc-core, sed, e2fsprogs, gettext, ncurses, zlib, perl
Provides: util-linux = %{version}

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
%setup -q


%build
%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	--enable-arch \
	--enable-init \
	--disable-kill \
	--enable-last \
	--enable-mesg \
	--enable-raw \
	--enable-rdev \
	--enable-write \
	--without-selinux \
	--without-audit \
	--with-fsprobe=blkid
make %{_smp_mflags}


%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"

make install DESTDIR="$RPM_BUILD_ROOT"
%find_lang util-linux-ng
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/ipc.info.gz %{_infodir}/dir

%postun
/sbin/ldconfig
/sbin/install-info --delete %{_infodir}/ipc.info.gz %{_infodir}/dir


%clean
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"


%files -f util-linux-ng.lang
%defattr(-, root, root)
%doc README* ABOUT-NLS AUTHORS COPYING DEPRECATED NEWS docs/*ReleaseNotes*
%doc TODO
/bin/arch
/bin/dmesg
/bin/more
/bin/*mount
/sbin/agetty
/sbin/blockdev
/sbin/cfdisk
/sbin/ctrlaltdel
/sbin/display-services
/sbin/fastboot
/sbin/fasthalt
/sbin/fdisk
/sbin/fsck.cramfs
/sbin/fsck.minix
/sbin/halt
/sbin/hwclock
/sbin/initctl
/sbin/losetup
/sbin/mkfs*
/sbin/need
/sbin/pivot_root
/sbin/provide
/sbin/raw
/sbin/reboot
/sbin/sfdisk
/sbin/shutdown
/sbin/simpleinit
/sbin/*swap*
%{_bindir}/cal
%{_bindir}/chkdupexe
%{_bindir}/chrt
%{_bindir}/col
%{_bindir}/colcrt
%{_bindir}/colrm
%{_bindir}/column
%{_bindir}/cytune
%{_bindir}/ddate
%{_bindir}/fdformat
%{_bindir}/flock
%{_bindir}/getopt
%{_bindir}/hexdump
%{_bindir}/i386
%{_bindir}/ionice
%{_bindir}/ipcrm
%{_bindir}/ipcs
%{_bindir}/isosize
%{_bindir}/last
%{_bindir}/line
%{_bindir}/linux32
%{_bindir}/linux64
%{_bindir}/logger
%{_bindir}/look
%{_bindir}/mcookie
%{_bindir}/mesg
%{_bindir}/namei
%{_bindir}/pg
%{_bindir}/rename
%{_bindir}/renice
%{_bindir}/rev
%{_bindir}/script
%{_bindir}/scriptreplay
%{_bindir}/setarch
%{_bindir}/setsid
%{_bindir}/setterm
%{_bindir}/tailf
%{_bindir}/taskset
%{_bindir}/ul
%{_bindir}/wall
%{_bindir}/whereis
%{_bindir}/write
%{_sbindir}/ramsize
%{_sbindir}/rdev
%{_sbindir}/readprofile
%{_sbindir}/rootflags
%{_sbindir}/rtcwake
%{_sbindir}/tunelp
%{_sbindir}/vidmode
%{_infodir}/ipc.info*
%{_mandir}/*/*
%{_datadir}/getopt/
