Name: e2fsprogs
Version: 1.41.8
Release: 3ev
Summary: Ext[234] Filesystem Utilities
URL: http://e2fsprogs.sourceforge.net/
Group: System Environment/Base
License: GPL-2, LGPL-2, MIT, BSD
Vendor: GNyU-Linux
Source: http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-uuidd.ii
BuildRequires(build,install): make, pkg-config, gettext
BuildRequires(build): gcc

%description
The ext2fsprogs package contains essential ext2 filesystem utilities which
consists of e2fsck, mke2fs, debugfs, dumpe2fs, tune2fs, and most of the other
core ext2 filesystem utilities.


%package -n libuuid1
Summary: Universally Unique Identifier library
Version: 1.2.0
Group: System Environment/Libraries
Conflicts: e2fsprogs < 1.41.0

%description -n libuuid1
The libuuid library generates and parses 128-bit universally unique ids
(UUIDs). A UUID is an identifier that is unique across both space and time,
with respect to the space of all UUIDs. A UUID can be used for multiple
purposes, from tagging objects with an extremely short lifetime, to reliably
identifying very persistent objects across a network.


%package -n uuidd
Summary: Universally Unique Identifier generation daemon
Group: System Environment/Daemons
Conflicts: e2fsprogs < 1.41.0
Obsoletes: uuid1

%description -n uuidd
The uuidd daemon is used by the UUID library to generate universally unique
identifiers (UUIDs), especially time-based UUID's in a secure and
guaranteed-unique fashion, even in the face of large numbers of threads trying
to grab UUID's running on different CPU's.


%package -n libblkid1
Version: 1.0
Group: System Environment/Libraries
Summary: A filesystem detection library
Conflicts: e2fsprogs < 1.41.0


%description -n libblkid1
A Library for filesystem detection by the means of the `blkid' program or
other, similar commands. This library provides an interface that allows to get
a file systems type, UUID and label (if any).


%package -n libcom_err2
Version: 2.1
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
	--sbindir=/sbin \
	--libdir='/%{_lib}' \
	--enable-fsck \
	--enable-e2initrd-helper \
	--enable-elf-shlibs 
%{__make} %{?_smp_mflags}
%{__make} check


%install
%{__make_install} install-libs DESTDIR='%{buildroot}'

# Libraries and utilites are sometimes needed at boot time, move them to /
# instead of /usr.
%{__mv} '%{buildroot}/%{_sbindir}' '%{buildroot}/sbin' ||:
%{__mkdir_p} '%{buildroot}/%{_libdir}'
%{__mv} '%{buildroot}/%{_lib}/pkgconfig' '%{buildroot}/%{_libdir}'

# Make sure socket and PID files are catalogized:
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/lib/libuuid'
%{__touch} '%{buildroot}/%{_localstatedir}/lib/libuuid/uuidd.pid'
%{__touch} '%{buildroot}/%{_localstatedir}/lib/libuuid/request'

# uuidd service file
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{install_ifile '%{SOURCE1}' 'daemon/uuidd.i'}

%{find_lang} 'e2fsprogs'

[[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ]] \
    && %{__rm} "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
%{__ldconfig}
update-info-dir


%postun
%{__ldconfig}
update-info-dir


%post -n libuuid1
%{__ldconfig}


%postun -n libuuid1
%{__ldconfig}


%preun -n uuidd
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/uuidd
	ng-update delete daemon/uuidd default
fi > /dev/null 2>&1
exit 0


%files -f e2fsprogs.lang
%defattr(-, root, root)
%doc ABOUT-NLS COPYING SHLIBS README RELEASE-NOTES  SUBMITTING-PATCHES
%config %{_sysconfdir}/mke2fs.conf
/sbin/*
%{_bindir}/*
/%{_lib}/libe2p.*
/%{_lib}/libext2fs.*
/%{_lib}/libss.*
/%{_lib}/e2initrd_helper
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


%files -n libuuid1
%defattr(-, root, root)
%doc lib/uuid/COPYING
%doc %{_mandir}/man3/uuid*.3*
%{_includedir}/uuid/
/%{_lib}/libuuid.*


%files -n uuidd
%defattr(-, root, root)
%doc COPYING
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/uuidd.i
%{_libdir}/pkgconfig/uuid.pc
%attr(0700, root, root) /sbin/uuidd
%doc %{_mandir}/man1/uuidgen.1*
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
