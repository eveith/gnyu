Name: e2fsprogs
Version: 1.39
Release: 1ev
Summary: Ext2 Filesystem Utilities
URL: http://e2fsprogs.sourceforge.net/
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Source: http://downloads.sourceforge.net/e2fsprogs/e2fsprogs-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make >= 3.79.1, gcc-core

%description
The ext2fsprogs package contains essential ext2 filesystem utilities which
consists of e2fsck, mke2fs, debugfs, dumpe2fs, tune2fs, and most of the other
core ext2 filesystem utilities.


%prep
%setup -q


%build
%configure \
	--enable-fsck \
	--enable-e2initrd-helper \
	--enable-elf-shlibs 
#	--enable-blkid-devmapper
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

# Install the complete library package. I wonder why these aren't installed by
# default?

mkdir -p "$RPM_BUILD_ROOT"/%{_mandir}/man3
for dir in blkid e2p et ext2fs ss uuid
do
	pushd lib/$dir
	make install DESTDIR="$RPM_BUILD_ROOT"
	popd
done

# Libraries and utilites are sometimes needed at boot time, move them to /
# instead of /usr.

mv "$RPM_BUILD_ROOT"/%{_sbindir} "$RPM_BUILD_ROOT"/sbin
mkdir -p "$RPM_BUILD_ROOT"/%{_lib}
mv "$RPM_BUILD_ROOT"/%{_libdir}/*.{so,a}* \
	"$RPM_BUILD_ROOT"/%{_libdir}/e2initrd_helper \
	"$RPM_BUILD_ROOT"/%{_lib}

%find_lang e2fsprogs

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
/sbin/install-info --info-dir=%{_infodir} %{_infodir}/libext2fs.info*

%postun
/sbin/ldconfig
/sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/libext2fs.info*


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files -f e2fsprogs.lang
%defattr(-, root, root)
%doc ABOUT-NLS COPYING ChangeLog README RELEASE-NOTES  SUBMITTING-PATCHES
%config /etc/mke2fs.conf
%{_mandir}/*/*
/sbin/*
%{_bindir}/*
%{_infodir}/libext2fs.info*
/%{_lib}/e2initrd_helper
/%{_lib}/*.so*
/%{_lib}/*.a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/blkid/
%{_includedir}/e2p/
%{_includedir}/et/
%{_includedir}/ext2fs/
%{_includedir}/ss/
%{_includedir}/uuid/
%{_datadir}/et/
%{_datadir}/ss/
