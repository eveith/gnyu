Summary: A screen manager that supports multiple logins on one terminal.
Name: screen
Version: 4.0.2
Release: 1ev
License: GPL2
Group: Applications/System
URL: http://www.gnu.org/software/screen
Prereq: /sbin/install-info, /usr/sbin/groupadd
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: ncurses texinfo pam libtool
Source0: ftp://ftp.uni-erlangen.de/pub/utilities/screen/screen-%{version}.tar.gz
Source1: screen.pam
Patch1: screen-3.9.13-ia64.patch
Patch2: screen-4.0.2-screenrc.patch
Patch3: screen-4.0.1-etcscreenrc.patch
Patch4: screen-3.9.11-utf8-install.patch
Patch5: screen-3.9.11-no-stripping-or-elf.patch

# The maintainers really didn't like this patch, and I couldn't
# reproduce the "access denied" problem on 4.0.1, so this 
# patch is not applied for now.  We'll include it in the srpm
# in case someone else wants it.
#
Patch6: screen-3.9.15-home-screendir.patch
Patch7: screen-4.0.1-args.patch
Patch8: screen-4.0.2-logname.patch
Patch9: screen-4.0.2-lock-shortcut.patch
Patch10: screen-4.0.2-lib64.patch

%description
The screen utility allows you to have multiple logins on just one
terminal. Screen is useful for users who telnet into a machine or are
connected via a dumb terminal, but want to use more than just one
login.

Install the screen package if you need a screen manager that can
support multiple logins on one terminal.


%prep
%setup -q
%patch1 -p1 -b .ia64
%patch2 -p1 -b .screenrc
#%patch3 -p1 -b .etcscreenrc
%patch4 -p1 -b .utf8-install
%patch5 -p1 -b .no-stripping-or-elf
#%patch8 -p1 -b .logname

# Uncomment if you want screen to first try to use $HOME/.screens
# and subsequently try to use /tmp/S-<user>
#
#%patch6 -p1 -b .screendir
%patch7 -p0 -b .args
%patch9 -p1 -b .lock-shortcut
%patch10 -p1 -b .lib64


%build
libtoolize --copy --force
autoconf

%configure \
	--enable-pam \
	--enable-colors256 \
	--enable-rxvt_osc \
	--enable-locale \
	--enable-telnet \
	--with-sys-screenrc="/etc/screenrc" \
	--with-socket-dir="/var/run/screen"

# We would like to have braille support.
#
sed -e 's/.*#.*undef.*HAVE_BRAILLE.*/#define HAVE_BRAILLE 1/;' \
		< config.h > config.tmp.h
mv config.tmp.h config.h

# We really don't want to be using /usr/local
# because we wish to be FSB complient
#
#sed -e 's/\/usr\/local\/etc/\/etc/g;' < etc/etcscreenrc > etc/etcscreenrc.tmp
#mv etc/etcscreenrc.tmp etc/etcscreenrc

find doc -type f | while read line; do
	sed -e 's/\(\/usr\)\?\/local\/etc/\/etc/g;' < $line > $line.tmp;
	mv $line.tmp $line
done

rm doc/screen.info*
make clean

CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" make $BUILD_MAKE_FLAGS


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc
%makeinstall DDESTDIR=$RPM_BUILD_ROOT

( cd $RPM_BUILD_ROOT
  rm -f .%{_bindir}/screen.old .%{_bindir}/screen
  mv .%{_bindir}/screen-%{version} .%{_bindir}/screen
)

install -c -m 0644 etc/etcscreenrc $RPM_BUILD_ROOT/etc/screenrc
cat etc/screenrc >> $RPM_BUILD_ROOT/etc/screenrc

# Better not forget to copy the pam file around
#
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
install -m 0644 $RPM_SOURCE_DIR/screen.pam $RPM_BUILD_ROOT/etc/pam.d/screen

# Create the socket dir
mkdir -p $RPM_BUILD_ROOT/var/run/screen

# Remove files from the buildroot which we don't want packaged
#
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir


%clean
rm -rf $RPM_BUILD_ROOT


%pre
groupadd -g 84 -f screen

%post
/sbin/install-info %{_infodir}/screen.info.gz %{_infodir}/dir --entry="* screen: (screen).             Terminal multiplexer."


%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete %{_infodir}/screen.info.gz %{_infodir}/dir --entry="* screen: (screen).             Terminal multiplexer."
fi

%postun
groupdel screen


%files
%defattr(-,root,root)
%doc NEWS README doc/FAQ doc/README.DOTSCREEN
%attr(2755,root,screen) %{_bindir}/screen
%attr(775,root,screen) %{_localstatedir}/run/screen
%{_datadir}/screen
%{_mandir}/man1/screen.1.gz
%{_infodir}/screen.info.gz
%config /etc/screenrc
%config /etc/pam.d/screen
