Name: tar
Version: 1.16.1
Release: 1ev
Summary: A utility for storing, backing up, and transporting files
URL: http://www.gnu.org/software/tar/
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Source: http://ftp.gnu.org/gnu/tar/tar-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make

%description
GNU `tar' saves many files together into a single tape or disk archive, and
can restore individual files from the archive. It includes multivolume
support, the ability to archive sparse files, automatic archive
compression/decompression, remote archives and special features that allow
`tar' to be used for incremental and full backups. It also includes `rmt', the
remote tape server (the `mt' tape drive control program is in GNU `cpio').


%prep
%setup -q


%build
%configure \
	--enable-backup-scripts
%{__make} %{_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir
%find_lang tar

# Move tar binary.
%{__mv} %{buildroot}/%{_bindir} %{buildroot}/bin 


%post
/sbin/ldconfig
update-info-dir
exit 0

%postun
/sbin/ldconfig
update-info-dir
exit 0


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__rm} -f tar.lang || :


%files -f tar.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog* NEWS README PORTS THANKS TODO
/bin/tar
%{_sbindir}/*
%{_infodir}/tar.info*
%{_libexecdir}/*
