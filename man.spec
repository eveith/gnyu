Name: man
Version: 1.6f
Release: 2ev
Summary: A set of documentation tools: man, apropos and whatis.
License: GPL
Group: System Environment/Base
Vendor: GNyU-Linux
Source0: http://primates.ximian.com/~flucifredi/man/man-%{version}.tar.gz
Source1: makewhatis.cronweekly
Source2: makewhatis.crondaily
Source3: mess.ru
Patch1: man-1.5m2-confpath.patch
Patch2: man-1.5h1-make.patch
Patch6: man-1.5m2-apropos.patch
Patch7: man-1.5m2-lc_all.patch
Patch10: man-1.5m2-i18n_makewhatis.patch
Patch12: man-1.5m2-posix.patch
Patch13: man-1.5p-makewhatis2.patch
Patch14: man-1.5p-makewhatis3.patch
Patch15: man-1.5p-mandirlist.patch
Patch16: man-1.5p-man2html.patch
Patch18: man-1.5p-pipe_makewhatis.patch
Patch19: man-1.5p-sec.patch
Patch20: man-1.5p-xorg.patch
Patch21: man-1.6b-i18n_nroff.patch
Patch22: man-1.6b-man-pages.patch
Patch23: man-1.6b-rpm.patch
Buildroot: %{_tmppath}/%{name}-root
Requires: less, groff >= 1.18, nroff-i18n, findutils, mktemp >= 1.5
Requires: bzip2, gzip, diffutils
BuildRequires: less, groff, bzip2, gzip

%description
The man package includes three tools for finding information and/or
documentation about your Linux system: man, apropos, and whatis. The
man system formats and displays on-line manual pages about commands or
functions on your system. Apropos searches the whatis database
(containing short descriptions of system commands) for a string.
Whatis searches its own database for a complete word.
The man package should be installed on your system because it is the
primary way to find documentation on a Linux system.


%prep
%setup -q
%patch1 -p1 -b .confpath
%patch2 -p1 -b .make
%patch6 -p1 -b .apropos
%patch12 -p1 -b .posix
%patch21 -p1 -b .i18n_nroff
%patch22 -p1 -b .up 

# Replace bad ru trans
%{__cp} -f %{SOURCE3} msgs

# Convert to UTF-8
for src in $(%{__find} msgs -type f -name 'mess.[a-z][a-z]')
do
	lang=$(echo "${src}" | %{__sed} -r 's;.*([a-z]{2})$;\1;')
	charset=
	case "$lang" in
		ja)
			charset=euc-jp
		;;
		ko)
			charset=euc-kr
		;;
		ru)
			charset=koi8-r
		;;
		da|de|en|es|fi|fr|it|pt|nl)
			charset=iso-8859-1
		;;
		cs|hr|pl|ro|sl)
			charset=iso-8859-2
		;;
		bg)
			charset=cp1251
		;;
		el)
			charset=iso-8859-7
		;;
		*)
			echo "*** LANGUAGE ${lang}: MUST SPECIFY CHARSET/ENCODING"
			exit 1
		;;
	esac

	iconv -t utf-8 -f "${charset}" -o "${src}.utf" "${src}" \
		&& %{__mv} "${src}.utf" "${src}"
done


%build
CFLAGS='%{optflags}'; CXXFLAGS='%{optflags}'; export CFLAGS CXXFLAGS
./configure \
	--prefix=%{_prefix} \
	--confdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	+fhs \
	+lang all 

%{__find} . -type f \
	| xargs %{__perl} -pi -e 's,man\.conf \(5\),man.config (5),g'
for i in $(%{__find} man -name man.conf.man)
do
	%{__mv} "$i" "${i%man.conf.man}man.config.5"
done

# HACK: Make output default to using -c; otherwise it appears broken.
%{__perl} -pi -e 's/nroff /nroff -c /' conf_script

touch Makefile	# make sure Make thinks we ran configure
%{__make} CC="%{_target_platform}-gcc $RPM_OPT_FLAGS"


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__mkdir_p} \
	'%{buildroot}'/etc/cron.{daily,weekly} \
	'%{buildroot}/%{_bindir}' \
	'%{buildroot}/%{_sbindir}'
%{__make_install} DESTDIR='%{buildroot}'

# Create man dirs
%{__find} '%{buildroot}/%{_mandir}' -type d -maxdepth 1 -mindepth 1 \
	-not -name "man*" > /tmp/mandirs

# This dir is not included by default
echo '%{buildroot}/%{_mandir}/en' >> /tmp/mandirs

while read dir
do
	for i in 1 2 3 4 5 6 7 8 9 n
	do
		%{__mkdir_p} "${dir}/man${i}"
	done
done < /tmp/mandirs
%{__rm} -f /tmp/mandirs

# Do another codepage-to-utf8-conversion
for src in $(find man -type f -name '*.[1-9n]')
do
	lang=$(echo ${src} | %{__sed} -r 's;.*/([a-z]{2})/.*;\1;')
	page=$(basename ${src})
	sect=$(echo ${page} | %{__sed} -r 's;.*([1-9n])$;man\1;')
	dir='%{buildroot}/%{_mandir}'
	case "$lang" in
		ja)
			charset=euc-jp
		;;
		ko)
			charset=euc-kr
		;;
		ru)
			charset=koi8-r
		;;
		da|de|en|es|fi|fr|it|pt|nl)
			charset=iso-8859-1
		;;
		cs|hr|pl|ro|sl)
			charset=iso-8859-2
		;;
		bg)
			charset=cp1251
		;;
		el)
			charset=iso-8859-7
		;;
		*)
			echo "*** LANGUAGE ${lang}: MUST SPECIFY CHARSET/ENCODING"
			exit 1
		;;
	esac

	%{__mkdir_p} "${dir}/${lang}/${sect}"
	iconv -t utf-8 -f "${charset}" -o "${dir}/${lang}/${sect}/${page}" "${src}"

	# ensure POSIX/C locale only has ASCII subset and no latin-1 
	if [[ "${lang}" = "en" ]]
	then
		%{__mkdir_p} "${dir}/${sect}"
		iconv -t ascii//translit -f "${charset}" \
			-o "${dir}/${sect}/${page}" "${src}"
	fi
done

# Install man config file and correct mappings and gunzip's position
%{__install} -m 0644 src/man.conf '%{buildroot}/%{_sysconfdir}/man.config'
mandir=$(echo '%{_mandir}' | %{__sed} 's/\//\\\//g')
%{__sed} -i "s/^\(MANPATH_MAP.*\)\/usr\/share\/man/\1${mandir}/" \
	'%{buildroot}/%{_sysconfdir}/man.config'
%{__sed} -i "s/\/usr\/bin\/gunzip/\/bin\/gunzip/" \
	'%{buildroot}/%{_sysconfdir}/man.config'


%{__install} -m 0755 '%{SOURCE1}' \
	'%{buildroot}/etc/cron.weekly/makewhatis.cron'
%{__install} -m 0755 '%{SOURCE2}' \
	'%{buildroot}/etc/cron.daily/makewhatis.cron'

cache='%{_localstatedir}/cache/man'
%{__mkdir_p} \
	"%{buildroot}/${cache}" \
	"%{buildroot}/${cache}/local" \
	"%{buildroot}/${cache}/X11R6"

for i in 1 2 3 4 5 6 7 8 9 n
do
	%{__mkdir_p} \
		"%{buildroot}/${cache}/cat${i}" \
		"%{buildroot}/${cache}/local/cat${i}" \
		"%{buildroot}/${cache}/X11R6/cat${i}"
done


# added man2html stuff
cd man2html
%makeinstall

for src in $(%{__find} '%{buildroot}/%{_mandir}' -type f -name '*.[1-9n]')
do
	%{__gzip} -9 "${src}"
done

# symlinks for manpath
(
	cd '%{buildroot}'
	%{__ln_s} man ./usr/bin/manpath
	%{__ln_s} man.1.gz ./%{_mandir}/man1/manpath.1.gz
)


%preun
cache='%{_localstatedir}/cache/man'
%{__rm} -f \
	"${cache}"/cat[123456789n]/* \
	"${cache}"/local/cat[123456789n]/* \
	"${cache}"/X11R6/cat[123456789n]/* \
	"${cache}/whatis" 2>/dev/null
exit 0


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-,root,root)
%doc README* COPYING HISTORY
%config %{_sysconfdir}/cron.weekly/makewhatis.cron
%config %{_sysconfdir}/cron.daily/makewhatis.cron
%config(noreplace) %{_sysconfdir}/man.config
%attr(0755,root,root) %{_bindir}/man
%{_bindir}/manpath
%{_bindir}/apropos
%{_bindir}/whatis
%{_sbindir}/makewhatis
%{_bindir}/man2html
%{_bindir}/man2dvi
%{_mandir}/man1/whatis.1*
%{_mandir}/man1/apropos.1*
%{_mandir}/man8/makewhatis.8*
%attr(0755,root,root) %dir %{_localstatedir}/cache/man
%attr(0775,root,man) %dir %{_localstatedir}/cache/man/cat[123456789n]
%attr(0775,root,man) %dir %{_localstatedir}/cache/man/local
%attr(0775,root,man) %dir %{_localstatedir}/cache/man/local/cat[123456789n]
%attr(0775,root,man) %dir %{_localstatedir}/cache/man/X11R6
%attr(0775,root,man) %dir %{_localstatedir}/cache/man/X11R6/cat[123456789n]
%dir %{_datadir}/locale/*/man
%dir %{_mandir}/*
%dir %{_mandir}/*/man*
%doc %{_mandir}/*/man?/*.*
