Name:
Version:
Release: 1ev
Summary:
URL:
Group:
License:
Vendor: GNyU-Linux
Source:
BuildRequires:

%description


%prep
%setup -q


%build


%install


[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post

%postun


%clean


%files
%defattr(-, root, root)
%doc 
