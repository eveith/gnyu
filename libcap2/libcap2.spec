Name: libcap2
Version: 2.19
Release: 2.0ev
Summary: A library for getting/setting POSIX.1e capabilities
URL: http://www.kernel.org/pub/linux/libs/security/linux-privs
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://www.kernel.org/pub/linux/libs/security/linux-privs/%{name}/libcap-%{version}.tar.gz
BuildRequires: make, perl, grep, gcc, libpam, libattr

%description
This is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.


%prep
%setup -q -n 'libcap-%{version}'


%build
%{__make} %{?_smp_mflags} \
	CC="${CC:-%{_target_platform}-gcc}" \
	COPTFLAGS="${CFLAGS:-%{optflags}}"
	


%install
%{__make} install \
	MANDIR='%{buildroot}/%{_mandir}' \
	SBINDIR='%{buildroot}/sbin' \
	INCDIR='%{buildroot}/%{_includedir}' \
	LIBDIR='%{buildroot}/%{_lib}'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc CHANGELOG License README
%doc progs
/%{_lib}/libcap.so*
/%{_lib}/libcap.a
%attr(0711, root, root) /%{_lib}/security/pam_cap.so
/sbin/capsh
/sbin/getcap
/sbin/getpcaps
/sbin/setcap
%{_includedir}/sys/capability.h
%doc %{_mandir}/man1/capsh.1*
%doc %{_mandir}/man3/cap_clear.3*
%doc %{_mandir}/man3/cap_clear_flag.3*
%doc %{_mandir}/man3/cap_compare.3*
%doc %{_mandir}/man3/cap_copy_ext.3*
%doc %{_mandir}/man3/cap_copy_int.3*
%doc %{_mandir}/man3/cap_dup.3*
%doc %{_mandir}/man3/cap_free.3*
%doc %{_mandir}/man3/cap_from_name.3*
%doc %{_mandir}/man3/cap_from_text.3*
%doc %{_mandir}/man3/cap_get_fd.3*
%doc %{_mandir}/man3/cap_get_file.3*
%doc %{_mandir}/man3/cap_get_flag.3*
%doc %{_mandir}/man3/cap_get_pid.3*
%doc %{_mandir}/man3/cap_get_proc.3*
%doc %{_mandir}/man3/cap_init.3*
%doc %{_mandir}/man3/cap_set_fd.3*
%doc %{_mandir}/man3/cap_set_file.3*
%doc %{_mandir}/man3/cap_set_flag.3*
%doc %{_mandir}/man3/cap_set_proc.3*
%doc %{_mandir}/man3/cap_size.3*
%doc %{_mandir}/man3/cap_to_name.3*
%doc %{_mandir}/man3/cap_to_text.3*
%doc %{_mandir}/man3/capgetp.3*
%doc %{_mandir}/man3/capsetp.3*
%doc %{_mandir}/man3/libcap.3*
%doc %{_mandir}/man8/getcap.8*
%doc %{_mandir}/man8/setcap.8*
