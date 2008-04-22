Name: gnu-gs-fonts
Version: 6.0
Release: 1ev
Summary: Fonts for PostScript interpreters
URL: http://www.gnu.org/software/ghostscript
Group: Applications/Text
License: GPL-2
Vendor: GNyU-Linux
Source0: ftp://ftp.gnu.org/gnu/ghostscript/%{name}-std-%{version}.tar.gz
Source1: ftp://ftp.gnu.org/gnu/ghostscript/%{name}-other-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils
Requires: ghostscript
BuildArch: noarch

%description
This package includes several free postscript fonts that are intended to be
used with Ghostscript interpreters, such as the GNU gs or espgs. They are 
especially useful with CUPS.


%prep
%setup -q -c -T -a 0 -a 1


%build
exit 0


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_datadir}/ghostscript/fonts'
%{__install} -m 0644 fonts/*.{afm,gsf,pfa,pfb} \
	'%{buildroot}/%{_datadir}/ghostscript/fonts/'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%dir %{_datadir}/ghostscript/fonts
%{_datadir}/ghostscript/fonts/*.afm
%{_datadir}/ghostscript/fonts/*.gsf
%{_datadir}/ghostscript/fonts/*.pfa
%{_datadir}/ghostscript/fonts/*.pfb
