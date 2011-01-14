Name: microcode_ctl
Version: 1.17
Release: 1ev
Summary: Userspace program for Intel IA32 CPU microcode updates
URL: http://www.urbanmyth.org/microcode/
Group: Systen Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.urbanmyth.org/microcode/microcode_ctl-%{version}.tar.gz
BuildRequires: make, gcc

%description
The microcode_ctl utility is a companion to the IA32 microcode driver
written by Tigran Aivazian <tigran@aivazian.fsnet.co.uk>. The utility has
two uses:
a) it decodes and sends new microcode to the kernel driver to be uploaded
   to Intel IA32 family processors. (Pentium Pro, PII, Celeron, PIII,
   Xeon, Pentium 4 etc, x86_64)
b) it signals the kernel driver to release any buffers it may hold
The microcode update is volatile and needs to be uploaded on each system
boot i.e. it doesn't reflash your cpu permanently, reboot and it reverts
back to the old microcode.


%prep
%setup -q


%build
%{__make} %{?_smp_mflags} \
	MICDIR='%{_sysconfdir}' \
	PREFIX='%{_prefix}' \
	INSDIR='/sbin'


%install
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}'
%{__mkdir_p} '%{buildroot}/sbin'
%{__mkdir_p} '%{buildroot}/%{_mandir}/man8'

%{__cp} microcode_ctl '%{buildroot}/sbin'
%{__cp} microcode_ctl.8 '%{buildroot}/%{_mandir}/man8'
%{__touch} '%{buildroot}/%{_sysconfdir}/microcode.dat'


%files
%defattr(-, root, root)
%doc README Changelog
%ghost %config %attr(0600, root, root) %{_sysconfdir}/microcode.dat
%attr(0700, root, root) /sbin/microcode_ctl
%doc %{_mandir}/man8/microcode_ctl.8*
