Name: e2fsprogs
Version: 1.41.0
Release: 2ev
Summary: Ext2 Filesystem Utilities
URL: http://e2fsprogs.sourceforge.net/
Group: System Environment/Base
License: GPL-2, LGPL-2, MIT, BSD
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/e2fsprogs/e2fsprogs-%{version}.tar.gz
Source1: %{name}-uuidd.ii
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires(build,install): make, pkg-config, gettext
BuildRequires(build): gcc
Requires: libblkid1, uuid1, libcom_err2

%description
The ext2fsprogs package contains essential ext2 filesystem utilities which
consists of e2fsck, mke2fs, debugfs, dumpe2fs, tune2fs, and most of the other
core ext2 filesystem utilities.


%package -n uuid1
Version: %{version}
Group: System Environment/Libraries
Summary: A subsystem to generate UUIDs
Conflicts: e2fsprogs < 1.41.0

%description -n uuid1
A library to generate universally unique identifiers (UUIDs), along with a
daemon that ensures time-based UUIDs to be guaranteed unique, even in the
face of threads trying to grab UUIDs running on different CPUs.


%package -n libblkid1
Version: %{version}
Group: System Environment/Libraries
Summary: A filesystem detection library
Conflicts: e2fsprogs < 1.41.0

%description -n libblkid1
A Library for filesystem detection by the means of the `blkid' program or
other, similar commands. This library provides an interface that allows to get
a file systems type, UUID and label (if any).


%package -n libcom_err2
Version: %{version}
Group: System Environment/Libraries
Summary: e2fsprogs common error reporting library
Conflicts: e2fsprogs < 1.41.0

%description -n libcom_err2
e2fsprogs is an error message display library, intended to be used with
e2fsprogs and similar utilities dealing with the file system.
Com_err displays  an error message on the standard error stream stderr (see
stdio(3S)) composed of the whoami string, which should specify the program 
name or some subportion of a program, followed by an error message generated 
from the code value (derived from compile_et(1)), and a string produced using 
the format string and any following arguments, in the same style as fprintf(3).


%prep
%setup -q


%build
%configure \
	--enable-fsck \
	--enable-e2initrd-helper \
	--enable-elf-shlibs 
%{__make} %{?_smp_mflags}
%{__make} check


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} install-libs DESTDIR='%{buildroot}'

# Libraries and utilites are sometimes needed at boot time, move them to /
# instead of /usr.
%{__mv} '%{buildroot}/%{_sbindir}' '%{buildroot}/sbin'
%{__mkdir_p} '%{buildroot}/%{_lib}'
%{__mv} '%{buildroot}/%{_libdir}'/*.* \
	'%{buildroot}/%{_lib}'

# Make sure socket and PID files are catalogized:
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/lib/libuuid'
touch  '%{buildroot}/%{_localstatedir}/lib/libuuid/uuidd.pid'
touch  '%{buildroot}/%{_localstatedir}/lib/libuuid/request'

# uuidd service file
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{__cat} < '%{SOURCE1}' | %{__sed} \
	-e 's,@uuidd@,/sbin/uuidd,g' \
	-e 's,@localstatedir@,%{_localstatedir},g' \
	> '%{buildroot}/%{_sysconfdir}/initng/daemon/uuidd.i'

%{find_lang} 'e2fsprogs'

[[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ]] \
    && %{__rm} "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
update-info-dir

%postun
/sbin/ldconfig
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f e2fsprogs.lang
%defattr(-, root, root)
%doc ABOUT-NLS COPYING SHLIBS README RELEASE-NOTES  SUBMITTING-PATCHES
%config %{_sysconfdir}/mke2fs.conf
/sbin/*
%{_bindir}/*
/%{_lib}/libe2p.*
/%{_lib}/libext2fs.*
/%{_lib}/libss.*
%{_libdir}/e2initrd_helper
%{_libdir}/pkgconfig/e2p.pc
%{_libdir}/pkgconfig/ext2fs.pc
%{_libdir}/pkgconfig/ss.pc
%{_includedir}/e2p/
%{_includedir}/et/
%{_includedir}/ext2fs/
%{_includedir}/ss/
%{_datadir}/et/
%{_datadir}/ss/
%doc %{_infodir}/libext2fs.info*
%doc %{_mandir}/man1/chattr.1*
%doc %{_mandir}/man1/compile_et.1*
%doc %{_mandir}/man1/lsattr.1*
%doc %{_mandir}/man1/mk_cmds.1*
%doc %{_mandir}/man5/e2fsck.conf.5*
%doc %{_mandir}/man5/mke2fs.conf.5*
%doc %{_mandir}/man8/badblocks.8*
%doc %{_mandir}/man8/blkid.8*
%doc %{_mandir}/man8/debugfs.8*
%doc %{_mandir}/man8/dumpe2fs.8*
%doc %{_mandir}/man8/e2fsck.8*
%doc %{_mandir}/man8/e2image.8*
%doc %{_mandir}/man8/e2label.8*
%doc %{_mandir}/man8/e2undo.8*
%doc %{_mandir}/man8/filefrag.8*
%doc %{_mandir}/man8/findfs.8*
%doc %{_mandir}/man8/fsck.8*
%doc %{_mandir}/man8/fsck.ext2.8*
%doc %{_mandir}/man8/fsck.ext3.8*
%doc %{_mandir}/man8/fsck.ext4.8*
%doc %{_mandir}/man8/fsck.ext4dev.8*
%doc %{_mandir}/man8/logsave.8*
%doc %{_mandir}/man8/mke2fs.8*
%doc %{_mandir}/man8/mkfs.ext2.8*
%doc %{_mandir}/man8/mkfs.ext3.8*
%doc %{_mandir}/man8/mkfs.ext4.8*
%doc %{_mandir}/man8/mkfs.ext4dev.8*
%doc %{_mandir}/man8/mklost+found.8*
%doc %{_mandir}/man8/resize2fs.8*
%doc %{_mandir}/man8/tune2fs.8*

%files -n libcom_err2
%defattr(-, root, root)
%doc %{_mandir}/man3/com_err.3*
/%{_lib}/libcom_err.*
%{_libdir}/pkgconfig/com_err.pc

%files -n uuid1
%defattr(-, root, root)
%doc lib/uuid/COPYING
%{_sysconfdir}/initng/daemon/uuidd.i
/%{_lib}/libuuid.*
%{_libdir}/pkgconfig/uuid.pc
%{_includedir}/uuid/
/sbin/uuidd
%doc %{_mandir}/man1/uuidgen.1*
%doc %{_mandir}/man3/uuid*.3*
%doc %{_mandir}/man8/uuidd.8*
%dir %{_localstatedir}/lib/libuuid
%ghost %config(missingok,noreplace) %{_localstatedir}/lib/libuuid/request
%ghost %config(missingok,noreplace) %{_localstatedir}/lib/libuuid/uuidd.pid

%files -n libblkid1
%defattr(-, root, root)
%doc %{_mandir}/man3/libblkid.3*
/%{_lib}/libblkid.*
%{_libdir}/pkgconfig/blkid.pc
%{_includedir}/blkid/
