Name: sed
Version: 4.2.1
Release: 2ev
Summary: The GNU Stream EDitor
URL: http://www.gnu.org/software/sed/
Group: System Environment/Base
License: GPL-3
Vendor: GNyU-Linux
Source: http://www.gnu.org/software/sed/%{name}-%{version}.tar.bz2
BuildRequires: make >= 3.79.1, gcc, libacl, gettext

%description
Sed (streams editor) isn't really a true text editor or text processor.
Instead, it is used to filter text, i.e., it takes text input and performs
some operation (or set of operations) on it and outputs the modified text. Sed
is typically used for extracting part of a file using pattern matching or
substituting multiple occurrences of a string within a file. 


%prep
%setup -q


%build
%configure \
	--bindir=/bin
%{__make} %{?_smp_mflags}
%{__make} check


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm_rf} "${RPM_BUILD_ROOT}/%{_infodir}/dir"
%{find_lang} sed


%post
update-info-dir


%preun
update-info-dir


%files -f sed.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS BUGS COPYING* ChangeLog README* NEWS THANKS
/bin/sed
%doc %{_infodir}/sed.info*
%doc %{_mandir}/man1/sed.1*
