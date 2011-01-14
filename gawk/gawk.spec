Name: gawk
Version: 3.1.7
Release: 2ev
Summary: A pattern scanning and processing language
URL: http://www.gnu.org/software/gawk
Group: System Environment/Base
License: GPL-3
Vendor: GNyU-Linux
Source: http://ftp.gnu.org/gnu/gawk/gawk-%{version}.tar.bz2
BuildRequires: make, gcc, gettext
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
%configure \
	--enable-switch \
	--enable-portals
%{__make} %{?_smp_mflags}
%{__make} check


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}" LDFLAGS="-s"
%{__rm} ${RPM_BUILD_ROOT}/%{_infodir}/dir ||:
%find_lang gawk

# Move awk to /bin where we need it at boot time
%{__mkdir_p} "${RPM_BUILD_ROOT}/bin"
%{__mv} -v "${RPM_BUILD_ROOT}/%{_bindir}"/*awk* "${RPM_BUILD_ROOT}/bin"


%post
update-info-dir


%postun
update-info-dir


%files -f gawk.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog* FUTURES LIMITATIONS POSIX* PROBLEMS
%doc README*
/bin/awk
/bin/gawk*
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
