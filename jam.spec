Name: jam
Version: 2.5
Release: 1ev
Summary: An open source build system like make especially for C/C++ code
URL: http://www.perforce.com/jam/jam.html
Group: Development/Tools
License: BSD
Vendor: GNyU-Linux
Source: ftp://ftp.perforce.com/jam/%{name}-%{version}.tar
BuildRequires: make, gcc, bison

%description
Jam is a software build tool that makes building simple things simple and
building complicated things manageable. It has been freely available as C
source for many years from the  Perforce Public Depot and is widely used to
build commercial and academic software. Jam is a very good solution for
conventional C/C++ compile-and-link builds.  Because Jam understands C/C++
dependencies, there is no need to declare header or object files.


%prep
	%setup -q


%build
	CFLAGS="${CFLAGS:-%{optflags}}"
	CXXFLAGS="${CXXFLAGS:-%{optflags}}"
	CC="${CC:-%{_target_platform}-gcc}"
	CXX="${CXX:-%{_target_platform}-g++}"
	export CFLAGS CXXFLAGS CC CXX

	%{__make} %{?_smp_mflags}
	%{__cp} bin.*/jam .
	./jam clean
	./jam \
		-s "CC=${CC}" \
		-s "C++=${CXX}" \
		-s "CCFLAGS=${CFLAGS}" \
		-s "C++FLAGS=${CXXFLAGS}"

%install
	./jam \
		-s BINDIR='%{buildroot}/%{_bindir}' \
		-s LIBDIR='%{buildroot}/%{_libdir}' \
		install


%files
	%defattr(-, root, root)
	%doc README RELNOTES *.html
	%{_bindir}/jam
