Name: poppler-data
Version: 0.2.1
Release: 1ev
Summary: Encoding data for use with poppler
URL: http://poppler.freedesktop.org/
Group: System Environment/Libraries
License: Proprietary, Adobe
Vendor: GNyU-Linux
Source: http://poppler.freedesktop.org/poppler-data-%{version}.tar.gz
BuildRequires: make
BuildArch: noarch

%description
This package consists of encoding files for use with poppler.  The
encoding files are optional and poppler will automatically read them
if they are present.  When installed, the encoding files enables
poppler to correctly render CJK and Cyrrilic properly.  While poppler
is licensed under the GPL, these encoding files are copyright Adobe
and licensed much more strictly, and thus distributed separately.


%prep
%setup -q


%build
exit 0


%install
%{__make} install DESTDIR='%{buildroot}' datadir='%{_datadir}'


%files
%defattr(-, root, root)
%doc README COPYING
%{_datadir}/poppler/
