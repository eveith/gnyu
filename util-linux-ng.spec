Name: util-linux-ng
Version: 2.16 
Release: 3ev
Summary: A random colleciton of important linux utilities
URL: http://userweb.kernel.org/~kzak/util-linux-ng/
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source0: ftp://ftp.kernel.org:/pub/linux/utils/%{name}/v2.16/%{name}-%{version}.tar.gz
BuildRequires: make, gcc, pkg-config >= 0.9.0, gettext
BuildRequires: libuuid1, libblkid1, zlib, ncurses
Provides: util-linux = %{version}

%description
A collection of very important linux utilities, such as: arch, dmesg, more,
mount, umount, agetty, blockdev, cfdisk, ctrlaltdel, fdisk, fsck, fsck.cramfs,
fsck.minix, hwclock, losetup, mkfs, mkfs.bfs, mkfs.cramfs, mkfs.minix, mkswap,
pivot_root, raw, sfdisk, swapoff, swapon, switch_root, cal, chkdupexe, chrt,
col, colcrt, colrm, column, cytune, ddate, flock, getopt, hexdump, i386,
ionice, ipcmk, ipcrm, ipcs, isosize, last, line, linux32, linux64, logger,
look, lscpu, mcookie, mesg, namei, pg, rename, renice, rev, script,
scriptreplay, setarch, setsid, setterm, tailf, taskset, ul, wall, whereis,
write, addpart, delpart, fdformat, ldattach, partx, readprofile, rtcwake, and
tunelp


%prep
%setup -q


%build
# We provide libuuid, uuidd, and libblkid through e2fsprogs.
%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	--disable-libuuid \
	--disable-uuidd \
	--disable-libblkid \
	--enable-arch \
	--disable-kill \
	--enable-last \
	--enable-mesg \
	--enable-partx \
	--enable-raw \
	--enable-write \
	--without-selinux \
	--without-audit 
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"
%find_lang util-linux-ng
%{__rm_rf} ${RPM_BUILD_ROOT}/%{_infodir}/dir

# Make sure the examples for getopt don't count in for dependencies
%{__chmod} 0644 '%{buildroot}/%{_datadir}/getopt'/*


%post
%{__ldconfig}
update-info-dir

%postun
%{__ldconfig}
update-info-dir


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
/sbin/fdisk
/sbin/fsck.cramfs
/sbin/fsck.minix
/sbin/fsck
/sbin/hwclock
/sbin/losetup
/sbin/mkfs*
/sbin/pivot_root
/sbin/raw
/sbin/sfdisk
/sbin/switch_root
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
%{_bindir}/flock
%{_bindir}/getopt
%{_bindir}/hexdump
%{_bindir}/i386
%{_bindir}/ionice
%{_bindir}/ipcmk
%{_bindir}/ipcrm
%{_bindir}/ipcs
%{_bindir}/isosize
%{_bindir}/last
%{_bindir}/line
%{_bindir}/linux32
%{_bindir}/linux64
%{_bindir}/logger
%{_bindir}/look
%{_bindir}/lscpu
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
%{_sbindir}/addpart
%{_sbindir}/delpart
%{_sbindir}/fdformat
%{_sbindir}/ldattach
%{_sbindir}/partx
%{_sbindir}/readprofile
%{_sbindir}/rtcwake
%{_sbindir}/tunelp
%doc %{_infodir}/ipc.info*
%doc %{_mandir}/man1/arch.1*
%doc %{_mandir}/man1/cal.1*
%doc %{_mandir}/man1/chkdupexe.1*
%doc %{_mandir}/man1/chrt.1*
%doc %{_mandir}/man1/col.1*
%doc %{_mandir}/man1/colcrt.1*
%doc %{_mandir}/man1/colrm.1*
%doc %{_mandir}/man1/column.1*
%doc %{_mandir}/man1/ddate.1*
%doc %{_mandir}/man1/dmesg.1*
%doc %{_mandir}/man1/flock.1*
%doc %{_mandir}/man1/getopt.1*
%doc %{_mandir}/man1/hexdump.1*
%doc %{_mandir}/man1/ionice.1*
%doc %{_mandir}/man1/ipcmk.1*
%doc %{_mandir}/man1/ipcrm.1*
%doc %{_mandir}/man1/ipcs.1*
%doc %{_mandir}/man1/last.1*
%doc %{_mandir}/man1/line.1*
%doc %{_mandir}/man1/logger.1*
%doc %{_mandir}/man1/look.1*
%doc %{_mandir}/man1/lscpu.1*
%doc %{_mandir}/man1/mcookie.1*
%doc %{_mandir}/man1/mesg.1*
%doc %{_mandir}/man1/more.1*
%doc %{_mandir}/man1/namei.1*
%doc %{_mandir}/man1/pg.1*
%doc %{_mandir}/man1/readprofile.1*
%doc %{_mandir}/man1/rename.1*
%doc %{_mandir}/man1/renice.1*
%doc %{_mandir}/man1/rev.1*
%doc %{_mandir}/man1/script.1*
%doc %{_mandir}/man1/scriptreplay.1*
%doc %{_mandir}/man1/setsid.1*
%doc %{_mandir}/man1/setterm.1*
%doc %{_mandir}/man1/tailf.1*
%doc %{_mandir}/man1/taskset.1*
%doc %{_mandir}/man1/ul.1*
%doc %{_mandir}/man1/wall.1*
%doc %{_mandir}/man1/whereis.1*
%doc %{_mandir}/man1/write.1*
%doc %{_mandir}/man5/fstab.5*
%doc %{_mandir}/man8/addpart.8*
%doc %{_mandir}/man8/agetty.8*
%doc %{_mandir}/man8/blockdev.8*
%doc %{_mandir}/man8/cfdisk.8*
%doc %{_mandir}/man8/ctrlaltdel.8*
%doc %{_mandir}/man8/cytune.8*
%doc %{_mandir}/man8/delpart.8*
%doc %{_mandir}/man8/fdformat.8*
%doc %{_mandir}/man8/fdisk.8*
%doc %{_mandir}/man8/fsck.8*
%doc %{_mandir}/man8/fsck.minix.8*
%doc %{_mandir}/man8/hwclock.8*
%doc %{_mandir}/man8/i386.8*
%doc %{_mandir}/man8/isosize.8*
%doc %{_mandir}/man8/ldattach.8*
%doc %{_mandir}/man8/linux32.8*
%doc %{_mandir}/man8/linux64.8*
%doc %{_mandir}/man8/losetup.8*
%doc %{_mandir}/man8/mkfs.8*
%doc %{_mandir}/man8/mkfs.bfs.8*
%doc %{_mandir}/man8/mkfs.minix.8*
%doc %{_mandir}/man8/mkswap.8*
%doc %{_mandir}/man8/mount.8*
%doc %{_mandir}/man8/partx.8*
%doc %{_mandir}/man8/pivot_root.8*
%doc %{_mandir}/man8/raw.8*
%doc %{_mandir}/man8/rtcwake.8*
%doc %{_mandir}/man8/setarch.8*
%doc %{_mandir}/man8/sfdisk.8*
%doc %{_mandir}/man8/swapoff.8*
%doc %{_mandir}/man8/swapon.8*
%doc %{_mandir}/man8/switch_root.8*
%doc %{_mandir}/man8/tunelp.8*
%doc %{_mandir}/man8/umount.8*
%dir %{_datadir}/getopt
%doc %{_datadir}/getopt/getopt*
