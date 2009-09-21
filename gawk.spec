Name: gawk
Version: 3.1.5
Release: 1ev
Summary: A pattern scanning and processing language.
URL: http://www.gnu.org/software/gawk
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://ftp.gnu.org/gnu/gawk/gawk-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1
Requires: /sbin/install-info
Provides: awk

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


%prep
%setup -q


%build
%configure --enable-switch --enable-portals
make


%install
make install DESTDIR="$RPM_BUILD_ROOT" LDFLAGS="-s"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir
%find_lang gawk

# Move awk to /bin where we need it at boot time
mkdir ${RPM_BUILD_ROOT}/bin
mv ${RPM_BUILD_ROOT}/%{_bindir}/*awk* ${RPM_BUILD_ROOT}/bin


%post
/sbin/install-info %{_infodir}/gawk.info.gz %{_infodir}/dir
/sbin/install-info %{_infodir}/gawkinet.info.gz %{_infodir}/dir

%postun
/sbin/install-info --delete %{_infodir}/gawk.info.gz %{_infodir}/dir
/sbin/install-info --delete %{_infodir}/gawkinet.info.gz %{_infodir}/dir


%clean
rm -rf ${RPM_BUILD_ROOT}


%files -f gawk.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog* FUTURES LIMITATIONS POSIX* PROBLEMS
%doc README*
/bin/awk
/bin/gawk
/bin/gawk*
/bin/igawk
/bin/pgawk*
%{_infodir}/gawk.info.gz
%{_infodir}/gawkinet.info.gz
%{_libexecdir}/awk/
%{_mandir}/man1/gawk.1*
%{_mandir}/man1/igawk.1*
%{_mandir}/man1/pgawk.1*
%{_datadir}/awk/
