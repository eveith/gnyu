Name: diffutils
Version: 2.8.1
Release: 1ev
Summary: This package contains the GNU diff, diff3, sdiff, and cmp utilities
URL: http://www.gnu.org/software/diffutils/
Group: Applications/Text
License: GPL-2
Vendor: MSP Slackware
Source: http://ftp.gnu.org/pub/gnu/diffutils/diffutils-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gettext

%description
Diffutils contains the GNU diff, diff3, sdiff, and cmp utilities. Their 
features are a superset of the Unix features and they are significantly 
faster. Cmp has been moved into this package from the GNU textutils package. 
These programs are usually used for creating patch files.


%prep
%setup -q


%build
%configure
%{__make} %{_smp_mflags}


%install
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang diffutils

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'


%files -f diffutils.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING NEWS README THANKS
%{_bindir}/cmp
%{_bindir}/*diff*
%{_infodir}/diff.info*
%{_mandir}/man1/cmp.1*
%{_mandir}/man1/diff.1*
%{_mandir}/man1/diff3.1*
%{_mandir}/man1/sdiff.1.*
