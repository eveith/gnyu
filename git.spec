Name: git
Version: 1.6.3.3
Release: 3ev
Summary: A distributed source code management system
URL: http://git-scm.org/
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: http://kernel.org/pub/software/scm/git/git-%{version}.tar.bz2
BuildRequires: make, gcc, perl, openssl, curl, expat, openssh, zlib
BuildRequires: asciidoc, xmlto
Requires: openssh, perl

%description
"git" can mean anything, depending on your mood.
 - random three-letter combination that is pronounceable, and not
   actually used by any common UNIX command.  The fact that it is a
   mispronunciation of "get" may or may not be relevant.
 - stupid. contemptible and despicable. simple. Take your pick from the
   dictionary of slang.
 - "global information tracker": you're in a good mood, and it actually
   works for you. Angels sing, and a light suddenly fills the room.
 - "goddamn idiotic truckload of sh*t": when it breaks
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.


%prep
	%setup -q


%build
	%configure \
		--without-tcltk
	%{__make} %{?_smp_mflags} all man


%install
	%{__make} install install-man DESTDIR='%{buildroot}' 

	# Move manpages *sigh*
	%{__mv} '%{buildroot}/%{_datadir}/man' '%{buildroot}/%{_mandir}' ||:
	%{__mv} '%{buildroot}/%{_mandir}/man'/* '%{buildroot}/%{_mandir}'
	%{__rm_rf} '%{buildroot}/%{_mandir}/man'

	# Remove Perl files we do not ship
	%{__rm} -rf '%{buildroot}/%{perl_archlib}'
	%{__rm} -rf '%{buildroot}/%{perl_sitearch}'


%files
	%defattr(-, root, root)
	%doc README COPYING Documentation/*.txt Documentation/howto
	%doc Documentation/technical
	%{_bindir}/git
	%{_bindir}/git-cvsserver
	%{_bindir}/git-receive-pack
	%{_bindir}/git-shell
	%{_bindir}/git-upload-archive
	%{_bindir}/git-upload-pack
	%{perl_sitelib}/Git.pm
	%dir %{_libexecdir}/git-core
	%{_libexecdir}/git-core/git-*
	%dir %{_datadir}/git-core
	%dir %{_datadir}/git-core/templates
	%{_datadir}/git-core/templates/description
	%dir %{_datadir}/git-core/templates/hooks
	%{_datadir}/git-core/templates/hooks/*.sample
	%dir %{_datadir}/git-core/templates/info
	%{_datadir}/git-core/templates/info/exclude
	%doc %{_mandir}/man3/Git.3pm*
	%doc %{_mandir}/man1/git-add.1*
	%doc %{_mandir}/man1/git-am.1*
	%doc %{_mandir}/man1/git-annotate.1*
	%doc %{_mandir}/man1/git-apply.1*
	%doc %{_mandir}/man1/git-archimport.1*
	%doc %{_mandir}/man1/git-archive.1*
	%doc %{_mandir}/man1/git-bisect.1*
	%doc %{_mandir}/man1/git-blame.1*
	%doc %{_mandir}/man1/git-branch.1*
	%doc %{_mandir}/man1/git-bundle.1*
	%doc %{_mandir}/man1/git-cat-file.1*
	%doc %{_mandir}/man1/git-check-attr.1*
	%doc %{_mandir}/man1/git-check-ref-format.1*
	%doc %{_mandir}/man1/git-checkout-index.1*
	%doc %{_mandir}/man1/git-checkout.1*
	%doc %{_mandir}/man1/git-cherry-pick.1*
	%doc %{_mandir}/man1/git-cherry.1*
	%doc %{_mandir}/man1/git-citool.1*
	%doc %{_mandir}/man1/git-clean.1*
	%doc %{_mandir}/man1/git-clone.1*
	%doc %{_mandir}/man1/git-commit-tree.1*
	%doc %{_mandir}/man1/git-commit.1*
	%doc %{_mandir}/man1/git-config.1*
	%doc %{_mandir}/man1/git-count-objects.1*
	%doc %{_mandir}/man1/git-cvsexportcommit.1*
	%doc %{_mandir}/man1/git-cvsimport.1*
	%doc %{_mandir}/man1/git-cvsserver.1*
	%doc %{_mandir}/man1/git-daemon.1*
	%doc %{_mandir}/man1/git-describe.1*
	%doc %{_mandir}/man1/git-diff-files.1*
	%doc %{_mandir}/man1/git-diff-index.1*
	%doc %{_mandir}/man1/git-diff-tree.1*
	%doc %{_mandir}/man1/git-diff.1*
	%doc %{_mandir}/man1/git-difftool.1*
	%doc %{_mandir}/man1/git-fast-export.1*
	%doc %{_mandir}/man1/git-fast-import.1*
	%doc %{_mandir}/man1/git-fetch-pack.1*
	%doc %{_mandir}/man1/git-fetch.1*
	%doc %{_mandir}/man1/git-filter-branch.1*
	%doc %{_mandir}/man1/git-fmt-merge-msg.1*
	%doc %{_mandir}/man1/git-for-each-ref.1*
	%doc %{_mandir}/man1/git-format-patch.1*
	%doc %{_mandir}/man1/git-fsck-objects.1*
	%doc %{_mandir}/man1/git-fsck.1*
	%doc %{_mandir}/man1/git-gc.1*
	%doc %{_mandir}/man1/git-get-tar-commit-id.1*
	%doc %{_mandir}/man1/git-grep.1*
	%doc %{_mandir}/man1/git-gui.1*
	%doc %{_mandir}/man1/git-hash-object.1*
	%doc %{_mandir}/man1/git-help.1*
	%doc %{_mandir}/man1/git-http-fetch.1*
	%doc %{_mandir}/man1/git-http-push.1*
	%doc %{_mandir}/man1/git-imap-send.1*
	%doc %{_mandir}/man1/git-index-pack.1*
	%doc %{_mandir}/man1/git-init-db.1*
	%doc %{_mandir}/man1/git-init.1*
	%doc %{_mandir}/man1/git-instaweb.1*
	%doc %{_mandir}/man1/git-log.1*
	%doc %{_mandir}/man1/git-lost-found.1*
	%doc %{_mandir}/man1/git-ls-files.1*
	%doc %{_mandir}/man1/git-ls-remote.1*
	%doc %{_mandir}/man1/git-ls-tree.1*
	%doc %{_mandir}/man1/git-mailinfo.1*
	%doc %{_mandir}/man1/git-mailsplit.1*
	%doc %{_mandir}/man1/git-merge-base.1*
	%doc %{_mandir}/man1/git-merge-file.1*
	%doc %{_mandir}/man1/git-merge-index.1*
	%doc %{_mandir}/man1/git-merge-one-file.1*
	%doc %{_mandir}/man1/git-merge-tree.1*
	%doc %{_mandir}/man1/git-merge.1*
	%doc %{_mandir}/man1/git-mergetool--lib.1*
	%doc %{_mandir}/man1/git-mergetool.1*
	%doc %{_mandir}/man1/git-mktag.1*
	%doc %{_mandir}/man1/git-mktree.1*
	%doc %{_mandir}/man1/git-mv.1*
	%doc %{_mandir}/man1/git-name-rev.1*
	%doc %{_mandir}/man1/git-pack-objects.1*
	%doc %{_mandir}/man1/git-pack-redundant.1*
	%doc %{_mandir}/man1/git-pack-refs.1*
	%doc %{_mandir}/man1/git-parse-remote.1*
	%doc %{_mandir}/man1/git-patch-id.1*
	%doc %{_mandir}/man1/git-peek-remote.1*
	%doc %{_mandir}/man1/git-prune-packed.1*
	%doc %{_mandir}/man1/git-prune.1*
	%doc %{_mandir}/man1/git-pull.1*
	%doc %{_mandir}/man1/git-push.1*
	%doc %{_mandir}/man1/git-quiltimport.1*
	%doc %{_mandir}/man1/git-read-tree.1*
	%doc %{_mandir}/man1/git-rebase.1*
	%doc %{_mandir}/man1/git-receive-pack.1*
	%doc %{_mandir}/man1/git-reflog.1*
	%doc %{_mandir}/man1/git-relink.1*
	%doc %{_mandir}/man1/git-remote.1*
	%doc %{_mandir}/man1/git-repack.1*
	%doc %{_mandir}/man1/git-repo-config.1*
	%doc %{_mandir}/man1/git-request-pull.1*
	%doc %{_mandir}/man1/git-rerere.1*
	%doc %{_mandir}/man1/git-reset.1*
	%doc %{_mandir}/man1/git-rev-list.1*
	%doc %{_mandir}/man1/git-rev-parse.1*
	%doc %{_mandir}/man1/git-revert.1*
	%doc %{_mandir}/man1/git-rm.1*
	%doc %{_mandir}/man1/git-send-email.1*
	%doc %{_mandir}/man1/git-send-pack.1*
	%doc %{_mandir}/man1/git-sh-setup.1*
	%doc %{_mandir}/man1/git-shell.1*
	%doc %{_mandir}/man1/git-shortlog.1*
	%doc %{_mandir}/man1/git-show-branch.1*
	%doc %{_mandir}/man1/git-show-index.1*
	%doc %{_mandir}/man1/git-show-ref.1*
	%doc %{_mandir}/man1/git-show.1*
	%doc %{_mandir}/man1/git-stage.1*
	%doc %{_mandir}/man1/git-stash.1*
	%doc %{_mandir}/man1/git-status.1*
	%doc %{_mandir}/man1/git-stripspace.1*
	%doc %{_mandir}/man1/git-submodule.1*
	%doc %{_mandir}/man1/git-svn.1*
	%doc %{_mandir}/man1/git-symbolic-ref.1*
	%doc %{_mandir}/man1/git-tag.1*
	%doc %{_mandir}/man1/git-tar-tree.1*
	%doc %{_mandir}/man1/git-unpack-file.1*
	%doc %{_mandir}/man1/git-unpack-objects.1*
	%doc %{_mandir}/man1/git-update-index.1*
	%doc %{_mandir}/man1/git-update-ref.1*
	%doc %{_mandir}/man1/git-update-server-info.1*
	%doc %{_mandir}/man1/git-upload-archive.1*
	%doc %{_mandir}/man1/git-upload-pack.1*
	%doc %{_mandir}/man1/git-var.1*
	%doc %{_mandir}/man1/git-verify-pack.1*
	%doc %{_mandir}/man1/git-verify-tag.1*
	%doc %{_mandir}/man1/git-web--browse.1*
	%doc %{_mandir}/man1/git-whatchanged.1*
	%doc %{_mandir}/man1/git-write-tree.1*
	%doc %{_mandir}/man1/git.1*
	%doc %{_mandir}/man1/gitk.1*
	%doc %{_mandir}/man5/gitattributes.5*
	%doc %{_mandir}/man5/githooks.5*
	%doc %{_mandir}/man5/gitignore.5*
	%doc %{_mandir}/man5/gitmodules.5*
	%doc %{_mandir}/man5/gitrepository-layout.5*
	%doc %{_mandir}/man7/gitcli.7*
	%doc %{_mandir}/man7/gitcore-tutorial.7*
	%doc %{_mandir}/man7/gitcvs-migration.7*
	%doc %{_mandir}/man7/gitdiffcore.7*
	%doc %{_mandir}/man7/gitglossary.7*
	%doc %{_mandir}/man7/gittutorial-2.7*
	%doc %{_mandir}/man7/gittutorial.7*
	%doc %{_mandir}/man7/gitworkflows.7*
