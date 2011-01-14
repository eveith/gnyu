Name: grub2
Version: 1.96
Release: 1ev
Summary: A boot loader: the GRand Unified Boot Loader (GRUB)
URL: http://www.gnu.org/software/grub/
Group: System Environment/Base
License: GPL-3
Vendor: GNyU-Linux
Source: ftp://alpha.gnu.org/gnu/grub/grub-%{version}.tar.gz
BuildRequires: make, gcc, bison, lzo >= 1.2

%description
GNU GRUB is a Multiboot boot loader. It was derived from GRUB, 
GRand Unified Bootloader, which was originally designed and implemented 
by Erich Stefan Boleyn.
Briefly, boot loader is the first software program that runs when a computer 
starts. It is responsible for loading and transferring control to the 
operating system kernel software (such as the Hurd or the Linux). The kernel, 
in turn, initializes the rest of the operating system (e.g. GNU).


%prep
%setup -q -n 'grub-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

%{__mkdir_p} '%{buildroot}/boot'
%{__touch} '%{buildroot}/boot/grub.cfg'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING DISTLIST NEWS README THANKS TODO
%attr(0640, root, root) /boot/grub.cfg
%dir %attr(0750, root, root) %{_sysconfdir}/grub.d
%{_sysconfdir}/grub.d/00_header                     
%{_sysconfdir}/grub.d/10_hurd                       
%{_sysconfdir}/grub.d/10_linux                      
%{_sysconfdir}/grub.d/README 
%{_bindir}/grub-mkimage
%{_bindir}/grub-mkrescue
%{_sbindir}/grub-install
%{_sbindir}/grub-mkdevicemap
%{_sbindir}/grub-probe
%{_sbindir}/grub-setup
%{_sbindir}/update-grub
%dir %{_libdir}/grub
%{_libdir}/grub/update-grub_lib
%dir %{_libdir}/grub/i386-pc
%{_libdir}/grub/i386-pc/*
