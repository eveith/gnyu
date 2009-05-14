Name: getmail
Version: 4.7.8
Release: 1ev
Summary: A mail retriever written in Python
URL: http://pyropus.ca/software/getmail/
Group: Applications/Internet
License: GPL-2
Vendor: MSP Slackware
Source: http://pyropus.ca/software/getmail/old-versions/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: python >= 2.3.3
Requires: python >= 2.3.3

%description
getmail is a mail retriever designed to allow you to get your mail from one 
or more mail accounts on various mail servers to your local machine for 
reading with a minimum of fuss. getmail is designed to be secure, flexible, 
reliable, and easy-to-use. getmail is designed to replace other mail retrievers
such as fetchmail.


%prep
%setup -q


%build
%{__python} setup.py build


%install
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'

# There's a bug where the setup.py script wants to copy a non-existent .spec
# file. :-/
touch getmail.spec

%{__python} setup.py install \
	--prefix=%{_prefix} \
	--root=%{buildroot} 

# No documentation cruft that's installed twice.
%{__rm} -rf %{buildroot}/%{_datadir}/doc

# And now we need to relocate manpages... urgh.
if [[ '%{_mandir}' != '%{_datadir}/man' ]]
then
	%{__mv} %{buildroot}/%{_datadir}/man %{buildroot}/%{_mandir}
fi


%clean
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README docs/*.html docs/*.css docs/*.txt
%doc docs/BUGS docs/CHANGELOG docs/THANKS docs/TODO docs/COPYING
%{_bindir}/getmail*
%{_libdir}/python*/site-packages/getmailcore/
%{_mandir}/man1/getmail*.1*
