# used for CVS snapshots:
%define CVSDATE %{nil}
%define WITH_SELINUX 0
%define desktop_file 0
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif

# Set this to 1 if you're building the enterprise version
%define enterprise 0
%define withruby 0

%if %{enterprise}
# don't include ruby interpreter
%define withnetbeans 0
%else
%define withnetbeans 1
%endif

%define withcvim 0


%define baseversion 7.0
#used for pre-releases:
%define beta %{nil}
%define vimdir vim70%{?beta}
%define patchlevel 042

Summary: The VIM editor.
Name: vim
Version: %{baseversion}.%{beta}%{patchlevel}
Release: 1ev
License: freeware
Group: Applications/Editors
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-%{baseversion}%{?beta}%{?CVSDATE}.tar.bz2
Source1: ftp://ftp.vim.org/pub/vim/extra/vim-%{baseversion}%{?beta}-lang%{?CVSDATE}.tar.gz
Source2: ftp://ftp.vim.org/pub/vim/extra/vim-%{baseversion}%{?beta}-extra%{?CVSDATE}.tar.gz
Source3: gvim.desktop
Source4: vimrc
#Source5: ftp://ftp.vim.org/pub/vim/patches/README.patches
Source6: spec.vim
Source7: gvim16.png
Source8: gvim32.png
Source9: gvim48.png
Source10: gvim64.png
Source11: Changelog.rpm
#Source12: vi-help.txt
# Source at http://www.vim.org/scripts/script.php?script_id=213 :
#Source12: cvim.zip
Patch2002: vim-7.0-fixkeys.patch
Patch2003: vim-6.2-specsyntax.patch
Patch2004: vim-7.0-crv.patch
Patch2010: xxd-locale.patch
# Patches 001 < 999 are patches from the base maintainer.
# If you're as lazy as me, generate the list using
# for i in `seq 1 14`; do printf "Patch%03d: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.%03d\n" $i $i; done
Patch001: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.001
Patch002: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.002
Patch003: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.003
Patch004: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.004
Patch005: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.005
Patch006: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.006
Patch007: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.007
Patch008: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.008
Patch009: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.009
Patch010: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.010
Patch011: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.011
Patch012: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.012
Patch013: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.013
Patch014: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.014
Patch015: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.015
Patch016: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.016
Patch017: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.017
Patch018: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.018
Patch019: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.019
Patch020: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.020
Patch021: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.021
Patch022: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.022
Patch023: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.023
Patch024: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.024
Patch025: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.025
Patch026: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.026
Patch027: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.027
Patch028: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.028
Patch029: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.029
Patch030: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.030
Patch031: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.031
Patch032: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.032
Patch033: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.033
Patch034: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.034
Patch035: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.035
Patch036: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.036
Patch037: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.037
Patch038: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.038
Patch039: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.039
Patch040: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.040
Patch041: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.041
Patch042: ftp://ftp.vim.org/pub/vim/patches/7.0/7.0.042
Patch3000: vim-7.0-syntax.patch
Patch3001: vim-6.2-rh1.patch
Patch3002: vim-6.1-rh2.patch
Patch3003: vim-6.1-rh3.patch
Patch3004: vim-7.0-rclocation.patch
Patch3005: vim-6.2-rh4.patch
#Patch3006: vim-6.2-rh5.patch
Patch3008: vim-6.4-cvim.patch
Patch3009: vim-6.4-checkhl.patch
Patch3010: vim-7.0-fstabsyntax.patch
Patch3011: vim-6.4-lib64.patch
Patch3012: vim-7.0-warning.patch
Patch3100: vim-selinux.patch
Patch3101: vim-selinux2.patch
Buildroot: %{_tmppath}/%{name}-%{version}-root
Buildrequires: python perl libtermcap gettext
Buildrequires: libacl gpm autoconf
%if "%{withruby}" == "1"
Buildrequires: ruby 
%endif
%if %{WITH_SELINUX}
Buildrequires: libselinux
%endif
%if %{desktop_file}
Requires: /usr/bin/desktop-file-install
BuildPrereq: desktop-file-utils >= %{desktop_file_utils_version}
%endif

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.


%package common
Summary: The common files needed by any version of the VIM editor.
Group: Applications/Editors
Obsoletes: vim7-common

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-common package contains files which every VIM binary will need in
order to run.

If you are installing vim-enhanced or vim-X11, you'll also need
to install the vim-common package.


%package minimal
Summary: A minimal version of the VIM editor.
Group: Applications/Editors
Obsoletes: vim
Obsoletes: vim7-minimal

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, which is
installed into /bin/vi for use when only the root partition is
present. NOTE: The online help is only available when the vim-common
package is installed.


%package enhanced
Summary: A version of the VIM editor which includes recent enhancements.
Group: Applications/Editors
Requires: vim-common = %{version}-%{release}
Obsoletes: vim-color
Obsoletes: vim7-enhanced

%description enhanced
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

Install the vim-enhanced package if you'd like to use a version of the
VIM editor which includes recently added enhancements like
interpreters for the Python and Perl scripting languages.  You'll also
need to install the vim-common package.


%package X11
Summary: The VIM version of the vi editor for the X Window System.
Group: Applications/Editors
Requires: vim-common = %{version}-%{release} libattr
BuildRequires: gtk2 libSM libXt
Prereq: gtk2 >= 2.6
Obsoletes: vim7-X11

%description X11
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and
more. VIM-X11 is a version of the VIM editor which will run within the
X Window System.  If you install this package, you can run VIM as an X
application with a full GUI interface and mouse support.

Install the vim-X11 package if you'd like to try out a version of vi
with graphics and mouse capabilities.  You'll also need to install the
vim-common package.


%prep
%setup -q -b 1 -n %{vimdir}
cp -f %{SOURCE6} runtime/ftplugin/spec.vim
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2002 -p1
%patch2003 -p1
%patch2004 -p1
%patch2010 -p1
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# Base patches...
# for i in `seq 1 14`; do printf "%%patch%03d -p0 \n" $i; done
%patch001 -p0
%patch002 -p0
%patch003 -p0
%patch004 -p0
# Win32:
#patch005 -p0
# MAC:
#patch006 -p0
%patch007 -p0
%patch008 -p0
%patch009 -p0
%patch010 -p0
%patch011 -p0
%patch012 -p0
%patch013 -p0
%patch014 -p0
%patch015 -p0
%patch016 -p0
%patch017 -p0
# VMS:
#patch018 -p0
%patch019 -p0
%patch020 -p0
%patch021 -p0
%patch022 -p0
%patch023 -p0
%patch024 -p0
%patch025 -p0
%patch026 -p0
# Win32
#patch027 -p0
# OS/2
#patch028 -p0
%patch029 -p0
%patch030 -p0
%patch031 -p0
# Win32
#patch032 -p0
%patch033 -p0
%patch034 -p0
%patch035 -p0
%patch036 -p0
%patch037 -p0
%patch038 -p0
%patch039 -p0
%patch040 -p0
%patch041 -p0
%patch042 -p0

%patch3000 -p1
%patch3001 -p1
%patch3002 -p1
%patch3003 -p1
%patch3004 -p1
#patch3005 -p1
#patch3006 -p1

%patch3009 -p1
%patch3010 -p1
%patch3011 -p1
%patch3012 -p1

%if %{WITH_SELINUX}
%patch3100 -p1
%patch3101 -p1
%endif

%if "%{withcvim}" == "1"
mkdir cvim
( cd cvim; unzip %{SOURCE12}; )
patch -p1 < %{PATCH3008}
%endif


%build
cd src
autoconf
#perl -pi -e "s,\\\$VIMRUNTIME,/usr/share/vim/%{vimdir},g" os_unix.h
#perl -pi -e "s,\\\$VIM,/usr/share/vim/%{vimdir}/macros,g" os_unix.h

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
%if "%{withruby}" == "1"
export  RUBY_CFLAGS=-I$(ruby -r rbconfig -e 'p Config::CONFIG["archdir"]')
%endif

%configure --with-features=huge --enable-pythoninterp --enable-perlinterp \
  --disable-tclinterp --with-x=yes \
  --enable-xim --enable-multibyte \
  --enable-gtk2-check --enable-gui=gtk2 \
  --with-compiledby="<bugzilla@redhat.com>" --enable-cscope \
  --with-modified-by="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp
%endif

make
cp vim gvim
make clean

%configure --prefix=/usr --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no \
 --enable-gui=no --exec-prefix=/usr --enable-multibyte \
 --enable-cscope --with-modified-by="<bugzilla@redhat.com>" \
 --with-compiledby="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp
%endif

make
cp vim enhanced-vim
make clean

#perl -pi -e "s/help.txt/vi-help.txt/"  os_unix.h ex_cmds.c
perl -pi -e "s/\/etc\/vimrc/\/etc\/virc/"  os_unix.h
%configure --prefix='${DEST}'/usr --with-features=tiny --with-x=no \
  --enable-multibyte \
  --disable-netbeans \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=termcap --enable-gui=no --disable-gpm --exec-prefix=/ --with-compiledby="<bugzilla@redhat.com>"

make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/vim}
#cp -f %{SOURCE5} .

%if "%{withcvim}" == "1"
# cvim plugin stuff:
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vim/%{vimdir}/codesnippets-c
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vim/%{vimdir}/plugin/templates
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vim/%{vimdir}/wordlists
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vim/%{vimdir}/rc
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vim/%{vimdir}/ftplugin
   install -m644 cvim/codesnippets-c/*  $RPM_BUILD_ROOT%{_datadir}/vim/%{vimdir}/codesnippets-c/
   install -m644 cvim/plugin/templates/*  $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/plugin/templates/
   install -m644 cvim/plugin/wrapper.sh  $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/plugin/
   install -m644 cvim/plugin/c.vim  $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/plugin/
   install -m644 cvim/plugin/templates/*  $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/plugin/templates/
   install -m644 cvim/rc/*  $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/rc/
   install -m644 cvim/wordlists/*  $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/wordlists/
   install -m644 cvim/ftplugin/*  $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/ftplugin/
   cp cvim/doc/* runtime/doc
   cp cvim/README.csupport .
%endif

cd src
%makeinstall BINDIR=/bin DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/usr/bin/xxd
make installmacros DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m755 gvim $RPM_BUILD_ROOT/usr/bin/gvim
install -m644 %{SOURCE7} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/gvim.png
install -m644 %{SOURCE8} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/gvim.png
install -m644 %{SOURCE9} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/gvim.png
install -m644 %{SOURCE10} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/gvim.png
install -m755 enhanced-vim $RPM_BUILD_ROOT/usr/bin/vim

( cd $RPM_BUILD_ROOT
  mv ./bin/vimtutor ./usr/bin/vimtutor
  mv ./bin/vim ./bin/vi
  rm -f ./bin/rvim
  ln -sf vi ./bin/ex
  ln -sf vi ./bin/rvi
  ln -sf vi ./bin/rview
  ln -sf vi ./bin/view
  ln -sf vim ./usr/bin/ex
  ln -sf vim ./usr/bin/rvim
  ln -sf vim ./usr/bin/vimdiff
  perl -pi -e "s,$RPM_BUILD_ROOT,," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvim.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz
  ln -sf gvim ./usr/bin/gview
  ln -sf gvim ./usr/bin/gex
  ln -sf gvim ./usr/bin/evim
  ln -sf gvim ./usr/bin/gvimdiff
  ln -sf vim.1.gz .%{_mandir}/man1/gvim.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/gvimdiff.1.gz
  ln -sf gvim ./usr/bin/vimx
  %if "%{desktop_file}" == "1"
    mkdir -p $RPM_BUILD_ROOT/usr/share/applications
    desktop-file-install --vendor net \
        --dir $RPM_BUILD_ROOT/usr/share/applications \
        --add-category "Application;Development;X-Red-Hat-Base" \
        %{SOURCE3}
  %else
    mkdir -p ./etc/X11/applnk/Applications
    cp %{SOURCE3} ./etc/X11/applnk/Applications/gvim.desktop
  %endif
  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./usr/share/vim/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

pushd $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/tutor
mkdir conv
   iconv -f CP1252 -t UTF8 tutor.ca > conv/tutor.ca
   iconv -f CP1252 -t UTF8 tutor.it > conv/tutor.it
   iconv -f CP1253 -t UTF8 tutor.gr > conv/tutor.gr
   iconv -f CP1252 -t UTF8 tutor.fr > conv/tutor.fr
   iconv -f CP1252 -t UTF8 tutor.es > conv/tutor.es
   iconv -f CP1252 -t UTF8 tutor.de > conv/tutor.de
   #iconv -f CP737 -t UTF8 tutor.gr.cp737 > conv/tutor.gr.cp737
   #iconv -f EUC-JP -t UTF8 tutor.ja.euc > conv/tutor.ja.euc
   #iconv -f SJIS -t UTF8 tutor.ja.sjis > conv/tutor.ja.sjis
   iconv -f UTF8 -t UTF8 tutor.ja.utf-8 > conv/tutor.ja.utf-8
   iconv -f UTF8 -t UTF8 tutor.ko.utf-8 > conv/tutor.ko.utf-8
   iconv -f CP1252 -t UTF8 tutor.no > conv/tutor.no
   iconv -f ISO-8859-2 -t UTF8 tutor.pl > conv/tutor.pl
   iconv -f ISO-8859-2 -t UTF8 tutor.sk > conv/tutor.sk
   iconv -f KOI8R -t UTF8 tutor.ru > conv/tutor.ru
   iconv -f CP1252 -t UTF8 tutor.sv > conv/tutor.sv
   mv -f tutor.gr.cp737 tutor.ja.euc tutor.ja.sjis tutor.ko.euc tutor.pl.cp1250 tutor.zh.big5 tutor.ru.cp1251 tutor.zh.euc conv/
   rm -f tutor.ca tutor.de tutor.es tutor.fr tutor.gr tutor.it tutor.ja.utf-8 tutor.ko.utf-8 tutor.no tutor.pl tutor.sk tutor.ru tutor.sv
mv -f conv/* .
rmdir conv
popd

# Dependency cleanups
chmod 644 $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/doc/vim2html.pl \
 $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/tools/*.pl \
 $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.sh <<EOF
if [ -n "\$BASH_VERSION" -o -n "\$KSH_VERSION" -o -n "\$ZSH_VERSION" ]; then
  [ -x /usr/bin/id ] || return
  [ \`/usr/bin/id -u\` -le 100 ] && return
  # for bash and zsh, only if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.csh <<EOF
[ -x /usr/bin/id ] || exit
[ \`/usr/bin/id -u\` -gt 100 ] && alias vi vim
EOF
chmod 0755 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/*
install -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/vimrc
install -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/virc
(cd $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/doc;
 gzip -9 *.txt
 gzip -d help.txt.gz
 cat tags | sed -e 's/\t\(.*.txt\)\t/\t\1.gz\t/;s/\thelp.txt.gz\t/\thelp.txt\t/' > tags.new; mv -f tags.new tags
# cp %{SOURCE12} . 
 )
(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;) 

# Remove some man pages which are provided by man-pages-{fr,it,pl}:
rm -f $RPM_BUILD_ROOT/%{_mandir}/pl/man1/{evim,ex,rview,rvim,view,vim,vimdiff,vimtutor}.1*
rm -f $RPM_BUILD_ROOT/%{_mandir}/fr/man1/{rview,view,vim,vimdiff,vimtutor}.1*
rm -f $RPM_BUILD_ROOT/%{_mandir}/it/man1/vim.1*


%post X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi

%postun X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi


%clean
rm -rf $RPM_BUILD_ROOT


%files common
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/vimrc
%doc README*
%doc runtime/docs
%doc $RPM_SOURCE_DIR/Changelog.rpm
%dir /usr/share/vim
%dir /usr/share/vim/%{vimdir}
/usr/share/vim/%{vimdir}/autoload
/usr/share/vim/%{vimdir}/colors
/usr/share/vim/%{vimdir}/compiler
/usr/share/vim/%{vimdir}/doc
#exclude /usr/share/vim/%{vimdir}/doc/vi-help.txt
/usr/share/vim/%{vimdir}/*.vim
/usr/share/vim/%{vimdir}/ftplugin
/usr/share/vim/%{vimdir}/indent
/usr/share/vim/%{vimdir}/keymap
/usr/share/vim/%{vimdir}/lang/*.vim
/usr/share/vim/%{vimdir}/lang/*.txt
%dir /usr/share/vim/%{vimdir}/lang
/usr/share/vim/%{vimdir}/macros
/usr/share/vim/%{vimdir}/plugin
/usr/share/vim/%{vimdir}/print
/usr/share/vim/%{vimdir}/spell
/usr/share/vim/%{vimdir}/syntax
/usr/share/vim/%{vimdir}/tools
/usr/share/vim/%{vimdir}/tutor
%lang(af) /usr/share/vim/%{vimdir}/lang/af
%lang(ca) /usr/share/vim/%{vimdir}/lang/ca
%lang(cs) /usr/share/vim/%{vimdir}/lang/cs
%lang(de) /usr/share/vim/%{vimdir}/lang/de
%lang(en_GB) /usr/share/vim/%{vimdir}/lang/en_GB
%lang(es) /usr/share/vim/%{vimdir}/lang/es
%lang(fr) /usr/share/vim/%{vimdir}/lang/fr
%lang(ga) /usr/share/vim/%{vimdir}/lang/ga
%lang(it) /usr/share/vim/%{vimdir}/lang/it
%lang(ja) /usr/share/vim/%{vimdir}/lang/ja
%lang(ko) /usr/share/vim/%{vimdir}/lang/ko
%lang(no) /usr/share/vim/%{vimdir}/lang/no
%lang(pl) /usr/share/vim/%{vimdir}/lang/pl
%lang(ru) /usr/share/vim/%{vimdir}/lang/ru
%lang(sk) /usr/share/vim/%{vimdir}/lang/sk
%lang(sv) /usr/share/vim/%{vimdir}/lang/sv
%lang(uk) /usr/share/vim/%{vimdir}/lang/uk
%lang(vi) /usr/share/vim/%{vimdir}/lang/vi
%lang(zh_CN) /usr/share/vim/%{vimdir}/lang/zh_CN
%lang(zh_TW) /usr/share/vim/%{vimdir}/lang/zh_TW
%lang(zh_CN.UTF-8) /usr/share/vim/%{vimdir}/lang/zh_CN.UTF-8
%lang(zh_TW.UTF-8) /usr/share/vim/%{vimdir}/lang/zh_TW.UTF-8
/usr/bin/xxd
%{_mandir}/man1/vim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/view.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/xxd.*
%lang(fr) %{_mandir}/fr*
%lang(it) %{_mandir}/it*
%lang(ru) %{_mandir}/ru*
%lang(pl) %{_mandir}/pl*

%files minimal
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/virc
/bin/ex
/bin/vi
/bin/view
/bin/rvi
/bin/rview
#/usr/share/vim/%{vimdir}/doc/vi-help.txt

%files enhanced
%defattr(-,root,root)
/usr/bin/vim
/usr/bin/rvim
/usr/bin/vimdiff
/usr/bin/ex
/usr/bin/vimtutor
%config %{_sysconfdir}/profile.d/vim.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*

%files X11
%defattr(-,root,root)
%if "%{desktop_file}" == "1"
/usr/share/applications/*
%else
/etc/X11/applnk/*/gvim.desktop
%endif
/usr/bin/gvim
/usr/bin/gvimdiff
/usr/bin/gview
/usr/bin/gex
/usr/bin/vimx
/usr/bin/evim
%{_mandir}/man1/evim.*
%{_mandir}/man1/gvim*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Tue Jul 25 2006 Karsten Hopp <karsten@redhat.de> 7.0.042-0.fc5
- patchlevel 42
- allow usage of VIM environment variable

* Wed Jul 12 2006 Karsten Hopp <karsten@redhat.de> 7.0.035-0.fc5.1
- fix a typo in http.conf syntax file

* Mon Jun 26 2006 Karsten Hopp <karsten@redhat.de> 7.0.035-0.fc5
- patchlevel 35
- remove conflicts with some man-page packages

* Wed Jun 21 2006 Karsten Hopp <karsten@redhat.de> 7.0.022-2
- add binfmt_misc rpc_pipefs to fstypes for better mtab highlighting

* Tue Jun 20 2006 Karsten Hopp <karsten@redhat.de> 7.0.022-1
- patchlevel 22

* Tue Jun 20 2006 Karsten Hopp <karsten@redhat.de> 7.0.020-1
- patchlevel 20

* Tue Jun 20 2006 Karsten Hopp <karsten@redhat.de> 7.0.019-1
- patchlevel 19
- buildrequire autoconf

* Tue May 30 2006 Karsten Hopp <karsten@redhat.de> 7.0.017-1
- patchlevel 17, although it affects just the Motif version
- own some directories (#192787)

* Sat May 13 2006 Karsten Hopp <karsten@redhat.de> 7.0.016-1
- patchlevel 016

* Fri May 12 2006 Karsten Hopp <karsten@redhat.de> 7.0.012-1
- patchlevel 012

* Thu May 11 2006 Karsten Hopp <karsten@redhat.de> 7.0.010-1
- patchlevel 010

* Wed May 10 2006 Karsten Hopp <karsten@redhat.de> 7.0.005-2
- patchlevel 005
- move older changelogs (<7.0) into a file, no need to keep them 
  in the rpm database

* Tue May 09 2006 Karsten Hopp <karsten@redhat.de> 7.0.000-2
- bump epoch, the buildsystem thinks 7.0.000-2 is older than 7.0.g001-1
  although rpm is quite happy with it.

* Mon May 08 2006 Karsten Hopp <karsten@redhat.de> 7.0.000-1
- vim-7.0 
- Spell checking support for about 50 languages
- Intelligent completion for C, HTML, Ruby, Python, PHP, etc.
- Tab pages, each containing multiple windows
- Undo branches: never accidentally lose text again
- Vim script supports Lists and Dictionaries (similar to Python)
- Vim script profiling
- Improved Unicode support
- Highlighting of cursor line, cursor column and matching braces
- Translated manual pages support.
- Internal grep; works on all platforms, searches compressed files
- Browsing remote directories, zip and tar archives
- Printing multi-byte text
- find details about the changes since vim-6.4 with :help version7

- fix SE Linux context of temporary (.swp) files (#189968)
- /bin/vi /vim-minimal is now using /etc/virc to avoid .rpmnew files
  when updating

* Tue May 02 2006 Karsten Hopp <karsten@redhat.de> 7.0.g001-1
- vim-7.0g BETA

* Fri Apr 28 2006 Karsten Hopp <karsten@redhat.de> 7.0.f001-1
- vim-7.0f3 BETA

* Thu Apr 20 2006 Karsten Hopp <karsten@redhat.de> 7.0.e001-1
- vim-7.0e BETA

* Tue Apr 11 2006 Karsten Hopp <karsten@redhat.de> 7.0.d001-1
- vim-7.0d BETA

* Fri Apr 07 2006 Karsten Hopp <karsten@redhat.de> 7.0c.000-3
- fix vimrc filename

* Thu Apr 06 2006 Karsten Hopp <karsten@redhat.de> 7.0c.000-2
- new snapshot

* Tue Apr 04 2006 Karsten Hopp <karsten@redhat.de> 7.0c.000-1
- vim-7.0c BETA

* Wed Mar 22 2006 Karsten Hopp <karsten@redhat.de> 7.0aa.000-3
- Rawhide build as vim, opposed to vim7 (prerelease)
- conflict with older man-pages-{it,fr} packages
- cleanup lang stuff

* Thu Mar 16 2006 Karsten Hopp <karsten@redhat.de> 7.0aa.000-2
- make it coexist with vim-6 (temporarily)
- new CVS snapshot

* Tue Mar 14 2006 Karsten Hopp <karsten@redhat.de> 7.0aa.000-1
- vim7 pre Release
- older changelogs available in Changelog.rpm

# vim:nrformats-=octal
