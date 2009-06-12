Name: screen
Version: 4.0.3
Release: 2ev
Summary: A screen manager that supports multiple logins on one terminal.
URL: http://www.gnu.org/software/screen
Group: Applications/System
License: GPL-2
Vendor: GNyU-Linux
Source0: ftp://ftp.uni-erlangen.de/pub/utilities/screen/screen-%{version}.tar.gz
Source1: screen.pam
Patch1: screen-3.9.13-ia64.patch
Patch2: screen-4.0.2-screenrc.patch
Patch3: screen-4.0.1-etcscreenrc.patch
Patch4: screen-3.9.11-utf8-install.patch
Patch5: screen-3.9.11-no-stripping-or-elf.patch
Patch6: screen-3.9.15-home-screendir.patch
Patch7: screen-4.0.1-args.patch
Patch8: screen-4.0.2-logname.patch
Patch9: screen-4.0.2-lock-shortcut.patch
Patch10: screen-4.0.2-lib64.patch
BuildRequires: make, gcc, libpam, ncurses, libutempter

%description
The screen utility allows you to have multiple logins on just one
terminal. Screen is useful for users who telnet into a machine or are
connected via a dumb terminal, but want to use more than just one
login.
Install the screen package if you need a screen manager that can
support multiple logins on one terminal.


%prep
	%setup -q


%build
	%configure \
		--enable-pam \
		--disable-socket-dir \
		--enable-colors256 \
		--enable-rxvt_osc \
		--enable-locale \
		--enable-telnet \
		--with-sys-screenrc='%{_sysconfdir}/screenrc'
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}'
	%{__cat} 'etc/screenrc' >> '%{buildroot}/%{_sysconfdir}/screenrc'
	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/pam.d'
	%{__cp} '%{SOURCE1}' '%{buildroot}/%{_sysconfdir}/pam.d/screen'
	%{__rm_rf} '%{buildroot}/%{_infodir}/dir'

	#pushd '%{buildroot}/%{_bindir}'
	#%{__ln_s} 'screen-%{version}' 'screen'
	#popd


%post
	update-info-dir


%preun
	update-info-dir


%files
	%defattr(-,root,root)
	%doc NEWS README doc/FAQ doc/README.DOTSCREEN
	%{_bindir}/screen
	%{_bindir}/screen-%{version}
	%{_datadir}/screen
	%doc %{_mandir}/man1/screen.1*
	%doc %{_infodir}/screen.info*
	%config(noreplace) %{_sysconfdir}/screenrc
	%config(noreplace) %{_sysconfdir}/pam.d/screen
