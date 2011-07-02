Name: gperf
Version: 3.0.4
Release: 1.0
Summary: A Compiler Tool for Generating Perfect Hash Functions
URL: http://www.gnu.org/software/gperf
Group: Development/Tools
License: GPL-3
Source: ftp://ftp.gnu.org/pub/gnu/gperf/gperf-%{version}.tar.gz
BuildRequires: grep, sed, make
BuildRequires: gcc-g++
BuildRequires: eglibc-devel, libstdc++-devel
Requires: info


%description
A perfect hash function is simply: a hash function and a data structure
that allows recognition of a key word in a set of words using exactly
one probe into the data structure.


%files
%defattr (-,root,root)
%doc README NEWS AUTHORS COPYING ChangeLog doc/*.html

%{_bindir}/gperf

%doc %{_infodir}/gperf.info*
%doc %{_mandir}/man1/gperf.1*


%post
if [ "$1" -eq 1 ]; then
    install-info %{_infodir}/gperf.info* '%{_infodir}/dir'
fi


%preun
if [ "$1" -eq 0 ]; then
    install-info --delete %{_infodir}/gperf.info* '%{_infodir}/dir'
fi


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

%{__rm_rf} '%{buildroot}%{_datadir}/doc'
[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check ||:
