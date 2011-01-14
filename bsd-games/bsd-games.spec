Name: bsd-games
Version: 2.17
Release: 1ev
Summary: A collection of textual games
URL: ftp://metalab.unc.edu/pub/Linux/games
Group: Amusements/Games
License: BSD
Vendor: MSP Slackware
Source0: ftp://metalab.unc.edu/pub/Linux/games/%{name}-%{version}.tar.gz
Source1: %{name}-login-fortune.sh
Source2: %{name}-login-fortune.csh
Patch0: %{name}-termcap_ospeed_redefinition.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: gcc-core, gcc-g++ ncurses, bison, flex
Requires: ncurses

%description
This is a collection of some of the text-based games and amusements that have
been enjoyed for decades on unix systems. 
Includes these programs: adventure, arithmetic, atc, backgammon, battlestar,
bcd, boggle, caesar, canfield, countmail, cribbage, dab, go-fish, gomoku,
hack, hangman, hunt, mille, monop, morse, number, pig, phantasia, pom, ppt,
primes, quiz, random, rain, robots, sail, snake, tetris, trek, wargames, worm,
worms, wump, wtf 


%prep
%setup -q
%patch -P 0 -p1


%build

# Configuring the BSD games involves creating a little shell script that
# carries the values we actually want the source to be configured to. 

cat << __END__ > config.params
	# Make the configure process non-interactive
	bsd_games_cfg_non_interactive='y'

	# Set installation prefix - this is $RPM_BUILD_ROOT.
	bsd_games_install_prefix="$RPM_BUILD_ROOT"
	install_prefix="$RPM_BUILD_ROOT"

	# We build all games - keep this empty.
	bsd_games_no_build_dirs='factor'

	# These directories contain the games we build - it is alot of stuff,
	# indeed. :^)
	bsd_games_def_build_dirs='quiz bcd fish caesar backgammon boggle wtf banner include morse sail pom monop arithmetic countmail battlestar hack wargames tetris hunt dab wump number rain cribbage primes dm tests ppt trek lib robots pig random fortune worm adventure snake gomoku mille canfield atc worms phantasia hangman'

	# Games target directory - yes, here we actually install into.
	bsd_games_gamesdir="%{_prefix}/games"

	# One game contains a daemon - huntd -, which we place in the gamesdir,
	# also.
	bsd_games_sbindir='%{_prefix}/games'

	# Fortune comes with an extra binary to create the fortune files
	# (strfile), which we place in /usr/bin.
	bsd_games_usrbindir='%{_bindir}'

	# "dm" is some pseudo-security feature, which enables you to restrict
	# access to the games to some groups. You can later link all games to the
	# "dm" binary, if you whish to.
	bsd_games_use_dm='n'
	bsd_games_libexecdir='%{_libdir}/games/dm'
	
	# We need to set some man page directories.
	bsd_games_man5dir='%{_mandir}/man5'
	bsd_games_man6dir='%{_mandir}/man6'
	bsd_games_man8dir='%{_mandir}/man8'

	# Aaah, the doc dir - don't worry about that, we'll copy the documentation
	# extra.
	bsd_games_docdir='%{_docdir}/%{name}-%{version}'

	# Keep some data stuff here
	bsd_games_sharedir='%{_datadir}/games'

	# Variable data stuff here...
	bsd_games_varlibdir='%{_localstatedir}/games'

	# We want to do a chown on installed files to make sure permissions are
	# sane.
	bsd_games_do_chown='y'

	# Set permissions, this is somewhat difficult. We could either make all
	# files world-writable, or set the games setgid to some special group.
	# None of all is really safe, so it's up to the user.
	binary='root root 0755'
	score_game='root root 0755'
	daemon='root root 0755'
	dmdir='root games 2755'
	manpage='root root 0644'
	constdata='root root 0644'
	vardata='root root 0644'
	vardata_perms_priv='0640'
	
	# This here is some manpages stuff - I don't really understand what
	# happens here, but the default is sane, AFAIK.
	bsd_games_use_dot_so='.so'
	bsd_games_gzip_manpages='n'
	
	# Set the C Compiler we use, the optimization and ld flags
	bsd_games_cc='%{_target_platform}-gcc'
	bsd_games_optimize_flags=''
	bsd_games_other_cflags="$RPM_OPT_FLAGS"
	bsd_games_other_ldflags=''

	# We keep the warning flags as they are, for both C and C++
	bsd_games_warning_flags='-Wall -W -Wstrict-prototypes -Wmissing-prototypes -Wpointer-arith -Wcast-align -Wcast-qual -Wwrite-strings'
	bsd_games_cxx_warning_flags='-Wall -W -Wpointer-arith -Wcast-align -Wcast-qual -Wwrite-strings'

	# We link against ncurses - be sure that the linker flag is correct.
	bsd_games_ncurses_lib='-lncurses'
	bsd_games_ncurses_includes='-I%{_includedir}/ncurses'

	# A game is able to use the OpenSSL library. Let it use SSL...
	bsd_games_use_libcrypto='y'
	bsd_games_openssl_lib='-lcrypto'
	bsd_games_openssl_includes='-I%{_includedir}/openssl'

	# We need a FLEX and YACC implementation. We use flex and bison.
	bsd_games_yacc='bison -y'
	bsd_games_lex='flex'
	bsd_games_lex_lib='-lfl'	

	# The default page we want to use is "less", set it here.
	bsd_games_pager='%{_bindir}/less'

	# Offensive fortune cookies are ok, really. :^)
	bsd_games_offensive_fortunes='y'
	
	# The game "sail" needs place to store some temporary files, which is ok.
	bsd_games_sail_dir='%{_localstatedir}/games/sail'
__END__

./configure
make %{_smp_mflags}
	


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install INSTALL_PREFIX="$RPM_BUILD_ROOT"

# Remove a piece of documentation we'll store elsewhere.
rm -rf "$RPM_BUILD_ROOT"/%{_datadir}/doc/bsd-games

# Install a profile script that prints out a fortune cookie at every login
mkdir -p "$RPM_BUILD_ROOT"/etc/profile.d
cp %{SOURCE1} %{SOURCE2} "$RPM_BUILD_ROOT"/etc/profile.d

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING NEWS SECURITY README THANKS TODO
%doc trek/USD.doc/trek.me
%attr(0755, root, root) /etc/profile.d/bsd-games-login-fortune.*
%{_bindir}/strfile
%{_prefix}/games/*
%{_datadir}/games/atc/
%{_datadir}/games/boggle/
%{_datadir}/games/*.instr
%{_datadir}/games/fortune/
%{_datadir}/games/monop-cards.pck
%{_datadir}/games/quiz/
%{_datadir}/games/wump.info
%{_datadir}/misc/acronyms*
%{_localstatedir}/games/hack/
%{_localstatedir}/games/phantasia/
