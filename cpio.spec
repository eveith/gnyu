Name: cpio
Version: 2.9
Release: 2ev
Summary: A tool to copy files into or out of a cpio or tar archive
URL: http://www.gnu.org/software/cpio/
Group: System Environment/Base
License: GPL
Vendor: GNyU-Linux
Source: http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, tar
Requires: tar

%description
GNU cpio copies files into or out of a cpio or tar archive. The archive can be
another file on the disk, a magnetic tape, or a pipe. GNU cpio supports the
following archive formats: binary, old ASCII, new ASCII, crc, HPUX binary,
HPUX old ASCII, old tar, and POSIX.1 tar. The tar format is provided for
compatability with the tar program. By default, cpio creates binary format
archives, for compatibility with older cpio programs. When extracting from
archives, cpio automatically recognizes which kind of archive it is reading
and can read archives created on machines with a different byte-order.


%prep
%setup -q


%build
%configure \
	--enable-mt \
	--with-rmt='%{_libexecdir}/rmt'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%find_lang cpio
%{__mv} "${RPM_BUILD_ROOT}/%{_bindir}" "${RPM_BUILD_ROOT}/bin"
%{__rm} -rf "${RPM_BUILD_ROOT}/%{_libexecdir}"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
%{__ldconfig}
update-info-dir
exit 0


%postun
%{__ldconfig}
update-info-dir


%files -f cpio.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README THANKS TODO
/bin/cpio
/bin/mt
%doc %{_mandir}/man1/*.1*
%doc %{_infodir}/cpio*.info*
