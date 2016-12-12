Name:
Version:
Release: 1.0
Summary:
URL:
Group:
License:
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


%files
%defattr(-, root, root)
%doc 
