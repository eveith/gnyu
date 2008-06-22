Name: sun-jdk
Version: 6.6
Release: 2ev
Summary: Sun's Java software development kit
URL: http://java.sun.com/
Group: Development/Languages
License: Proprietary
Vendor: GNyU-Linux
Source: jdk-6u6-linux-i586.bin
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: bash, coreutils
Provides: java-jdk, java-sdk, jdk

%description
The Java SE Development Kit (JDK) includes the Java Runtime Environment (JRE)
and command-line development tools that are useful for developing applets and
applications.


%prep
exit 0


%build
exit 0


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'

%{__mkdir_p} '%{buildroot}/%{_libdir}'
pushd '%{buildroot}/%{_libdir}'

alias more=true
echo 'yes' | sh '%{SOURCE0}'
unalias more

%{__ln_s} jdk1.6.0_06 jdk-%{version}
%{__ln_s} jdk1.6.0_06 java

popd


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc %{_libdir}/jdk1.6.0_??/sample 
%{_libdir}/jdk1.6.0_??
%{_libdir}/jdk-%{version}
%{_libdir}/java
