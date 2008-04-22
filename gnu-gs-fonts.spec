Name:
Version:
Release: 1ev
Summary:
URL:
Group:
License:
Vendor: GNyU-Linux
Source:
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires:

%description


%prep
%setup -q


%build


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post

%postun


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc 
