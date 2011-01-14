Name: tar
Version: 1.22
Release: 2ev
Summary: A utility for storing, backing up, and transporting files
URL: http://www.gnu.org/software/tar/
Group: System Environment/Base
License: GPL-3
Vendor: GNyU-Linux
Source: http://ftp.gnu.org/gnu/tar/tar-%{version}.tar.bz2
BuildRequires: make, gcc, gettext

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
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__rm} -f '%{buildroot}/%{_infodir}/dir'
	%find_lang tar

	# Move tar binary.
	%{__mv} '%{buildroot}/%{_bindir}' '%{buildroot}/bin'


%post
	update-info-dir
	exit 0


%postun
	update-info-dir
	exit 0


%files -f tar.lang
	%defattr(-, root, root)
	%doc ABOUT-NLS AUTHORS COPYING ChangeLog* NEWS README PORTS THANKS TODO
	/bin/tar
	%{_sbindir}/backup
	%{_sbindir}/restore
	%doc %{_infodir}/tar.info*
	%{_libexecdir}/backup.sh
	%{_libexecdir}/dump-remind
	%{_libexecdir}/rmt
