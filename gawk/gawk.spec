Name: gawk
Version: 4.0.0
Release: 1.0
Summary: A pattern scanning and processing language
URL: http://www.gnu.org/software/gawk
Group: System Environment/Base
License: GPL-3
Source: http://ftp.gnu.org/gnu/gawk/gawk-%{version}.tar.xz
BuildRequires: grep, sed, gawk, make
BuildRequires: bison, gcc
BuildRequires: gettext-tools >= 0.18.1
BuildRequires: eglibc-devel, readline-devel
Provides: awk = %{version}-%{release}
Requires: info

%description
If you are like many computer users, you would frequently like to make changes
in various text files wherever certain patterns appear, or extract data from
parts of certain lines while discarding the rest. To write a program to do
this in a language such as C or Pascal is a time-consuming inconvenience that
may take many lines of code. The job is easy with awk, especially the GNU
implementation: gawk. 
The awk utility interprets a special-purpose programming language that makes
it possible to handle simple data-reformatting jobs with just a few lines of
code.


%files -f gawk.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog* FUTURES LIMITATIONS POSIX* PROBLEMS
%doc README*

/bin/awk
/bin/gawk*
/bin/dgawk
/bin/igawk
/bin/pgawk*

%doc %{_infodir}/gawk.info*
%doc %{_infodir}/gawkinet.info*

%dir %{_libexecdir}/awk
%{_libexecdir}/awk/??cat

%doc %{_mandir}/man1/gawk.1*
%doc %{_mandir}/man1/igawk.1*
%doc %{_mandir}/man1/pgawk.1*

%dir %{_datadir}/awk
%{_datadir}/awk/*.awk


%post
if [ "$1" -eq 1 ]; then
    install-info %{_infodir}/gawk.info* '%{_infodir}/dir'
fi


%preun
if [ "$1" -eq 0 ]; then
    install-info --delete %{_infodir}/gawk.info* '%{_infodir}/dir'
fi


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang gawk

%{__rm} ${RPM_BUILD_ROOT}/%{_infodir}/dir ||:

# Move awk to /bin where we need it at boot time

%{__mv} '%{buildroot}%{_bindir}' '%{buildroot}/bin'


%check
%{__make} check ||:
