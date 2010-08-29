Name: git
Version: 1.7.2.2
Release: 4.0ev
Summary: A distributed source code management system
URL: http://git-scm.org/
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: http://kernel.org/pub/software/scm/git/git-%{version}.tar.bz2
BuildRequires: make, gcc
BuildRequires: perl, python, diffutils
BuildRequires: openssl, curl, expat, openssh, zlib
BuildRequires: asciidoc >= 7.0.0, xmlto
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


%package web
Summary: A web frontend to Git
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description
Gitweb is a simple HTTP fronted to Git repositories, allowing online browsing
if the sources, patches, patchsets and commits.


%package python
Summary: Python bindings for interacting with Git repositories
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description python
This package provides the Python bindings to Git. It allows accessing Git
repositories in a programmatic way via Python.


%package perl
Summary: Perl bindings for Git
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description perl
git-perl provides Perl bindings to Git. It is used to provide a Perl API to
git and git repositories. git-perl is needed for "git-add -i" and "git-add
-p", so it's suggested you install it along with the main package.


%package cvs
Summary: CVS-to-Git migration tools, including a CVS server
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description cvs
The CVS package allows to easily migrate from CVS to Git. It even features a
fake CVS server that uses Git internally. It thus allows people to painlessly
switch from a CVS environment to a Git one, and use the CVS tools and
frontends as long as one whishes to.


%package svn
Summary: SVN-to-Git migration tools
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description svn
This package contains tools that allow a rather painless migration from a SVN
repository to Git.




%prep
%setup -q


%build
%configure \
	--with-curl \
	--with-expat \
	--without-tcltk
%{__make} %{?_smp_mflags} all man


%install
%{__make} install install-man DESTDIR='%{buildroot}' 

%{__mkdir} '%{buildroot}/%{_sysconfdir}'
%{__touch} '%{buildroot}/%{_sysconfdir}/gitconfig'

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
%ghost %config %{_sysconfdir}/gitconfig
%{_bindir}/git
%{_bindir}/git-receive-pack
%{_bindir}/git-shell
%{_bindir}/git-upload-archive
%{_bindir}/git-upload-pack
%dir %{_libexecdir}/git-core
%{_libexecdir}/git-core/git
%{_libexecdir}/git-core/git-add
%{_libexecdir}/git-core/git-add--interactive
%{_libexecdir}/git-core/git-am
%{_libexecdir}/git-core/git-annotate
%{_libexecdir}/git-core/git-apply
%{_libexecdir}/git-core/git-archimport
%{_libexecdir}/git-core/git-archive
%{_libexecdir}/git-core/git-bisect
%{_libexecdir}/git-core/git-bisect--helper
%{_libexecdir}/git-core/git-blame
%{_libexecdir}/git-core/git-branch
%{_libexecdir}/git-core/git-bundle
%{_libexecdir}/git-core/git-cat-file
%{_libexecdir}/git-core/git-check-attr
%{_libexecdir}/git-core/git-check-ref-format
%{_libexecdir}/git-core/git-checkout
%{_libexecdir}/git-core/git-checkout-index
%{_libexecdir}/git-core/git-cherry
%{_libexecdir}/git-core/git-cherry-pick
%{_libexecdir}/git-core/git-clean
%{_libexecdir}/git-core/git-clone
%{_libexecdir}/git-core/git-commit
%{_libexecdir}/git-core/git-commit-tree
%{_libexecdir}/git-core/git-config
%{_libexecdir}/git-core/git-count-objects
%{_libexecdir}/git-core/git-daemon
%{_libexecdir}/git-core/git-describe
%{_libexecdir}/git-core/git-diff
%{_libexecdir}/git-core/git-diff-files
%{_libexecdir}/git-core/git-diff-index
%{_libexecdir}/git-core/git-diff-tree
%{_libexecdir}/git-core/git-difftool
%{_libexecdir}/git-core/git-difftool--helper
%{_libexecdir}/git-core/git-fast-export
%{_libexecdir}/git-core/git-fast-import
%{_libexecdir}/git-core/git-fetch
%{_libexecdir}/git-core/git-fetch-pack
%{_libexecdir}/git-core/git-filter-branch
%{_libexecdir}/git-core/git-fmt-merge-msg
%{_libexecdir}/git-core/git-for-each-ref
%{_libexecdir}/git-core/git-format-patch
%{_libexecdir}/git-core/git-fsck
%{_libexecdir}/git-core/git-fsck-objects
%{_libexecdir}/git-core/git-gc
%{_libexecdir}/git-core/git-get-tar-commit-id
%{_libexecdir}/git-core/git-grep
%{_libexecdir}/git-core/git-hash-object
%{_libexecdir}/git-core/git-help
%{_libexecdir}/git-core/git-http-backend
%{_libexecdir}/git-core/git-http-fetch
%{_libexecdir}/git-core/git-http-push
%{_libexecdir}/git-core/git-imap-send
%{_libexecdir}/git-core/git-index-pack
%{_libexecdir}/git-core/git-init
%{_libexecdir}/git-core/git-init-db
%{_libexecdir}/git-core/git-instaweb
%{_libexecdir}/git-core/git-log
%{_libexecdir}/git-core/git-lost-found
%{_libexecdir}/git-core/git-ls-files
%{_libexecdir}/git-core/git-ls-remote
%{_libexecdir}/git-core/git-ls-tree
%{_libexecdir}/git-core/git-mailinfo
%{_libexecdir}/git-core/git-mailsplit
%{_libexecdir}/git-core/git-merge
%{_libexecdir}/git-core/git-merge-base
%{_libexecdir}/git-core/git-merge-file
%{_libexecdir}/git-core/git-merge-index
%{_libexecdir}/git-core/git-merge-octopus
%{_libexecdir}/git-core/git-merge-one-file
%{_libexecdir}/git-core/git-merge-ours
%{_libexecdir}/git-core/git-merge-recursive
%{_libexecdir}/git-core/git-merge-resolve
%{_libexecdir}/git-core/git-merge-subtree
%{_libexecdir}/git-core/git-merge-tree
%{_libexecdir}/git-core/git-mergetool
%{_libexecdir}/git-core/git-mergetool--lib
%{_libexecdir}/git-core/git-mktag
%{_libexecdir}/git-core/git-mktree
%{_libexecdir}/git-core/git-mv
%{_libexecdir}/git-core/git-name-rev
%{_libexecdir}/git-core/git-notes
%{_libexecdir}/git-core/git-pack-objects
%{_libexecdir}/git-core/git-pack-redundant
%{_libexecdir}/git-core/git-pack-refs
%{_libexecdir}/git-core/git-parse-remote
%{_libexecdir}/git-core/git-patch-id
%{_libexecdir}/git-core/git-peek-remote
%{_libexecdir}/git-core/git-prune
%{_libexecdir}/git-core/git-prune-packed
%{_libexecdir}/git-core/git-pull
%{_libexecdir}/git-core/git-push
%{_libexecdir}/git-core/git-quiltimport
%{_libexecdir}/git-core/git-read-tree
%{_libexecdir}/git-core/git-rebase
%{_libexecdir}/git-core/git-rebase--interactive
%{_libexecdir}/git-core/git-receive-pack
%{_libexecdir}/git-core/git-reflog
%{_libexecdir}/git-core/git-relink
%{_libexecdir}/git-core/git-remote
%{_libexecdir}/git-core/git-remote-ftp
%{_libexecdir}/git-core/git-remote-ftps
%{_libexecdir}/git-core/git-remote-http
%{_libexecdir}/git-core/git-remote-https
%{_libexecdir}/git-core/git-repack
%{_libexecdir}/git-core/git-replace
%{_libexecdir}/git-core/git-repo-config
%{_libexecdir}/git-core/git-request-pull
%{_libexecdir}/git-core/git-rerere
%{_libexecdir}/git-core/git-reset
%{_libexecdir}/git-core/git-rev-list
%{_libexecdir}/git-core/git-rev-parse
%{_libexecdir}/git-core/git-revert
%{_libexecdir}/git-core/git-rm
%{_libexecdir}/git-core/git-send-email
%{_libexecdir}/git-core/git-send-pack
%{_libexecdir}/git-core/git-sh-setup
%{_libexecdir}/git-core/git-shell
%{_libexecdir}/git-core/git-shortlog
%{_libexecdir}/git-core/git-show
%{_libexecdir}/git-core/git-show-branch
%{_libexecdir}/git-core/git-show-index
%{_libexecdir}/git-core/git-show-ref
%{_libexecdir}/git-core/git-stage
%{_libexecdir}/git-core/git-stash
%{_libexecdir}/git-core/git-status
%{_libexecdir}/git-core/git-stripspace
%{_libexecdir}/git-core/git-submodule
%{_libexecdir}/git-core/git-symbolic-ref
%{_libexecdir}/git-core/git-tag
%{_libexecdir}/git-core/git-tar-tree
%{_libexecdir}/git-core/git-unpack-file
%{_libexecdir}/git-core/git-unpack-objects
%{_libexecdir}/git-core/git-update-index
%{_libexecdir}/git-core/git-update-ref
%{_libexecdir}/git-core/git-update-server-info
%{_libexecdir}/git-core/git-upload-archive
%{_libexecdir}/git-core/git-upload-pack
%{_libexecdir}/git-core/git-var
%{_libexecdir}/git-core/git-verify-pack
%{_libexecdir}/git-core/git-verify-tag
%{_libexecdir}/git-core/git-web--browse
%{_libexecdir}/git-core/git-whatchanged
%{_libexecdir}/git-core/git-write-tree
%dir %{_datadir}/git-core
%dir %{_datadir}/git-core/templates
%{_datadir}/git-core/templates/description
%dir %{_datadir}/git-core/templates/hooks
%{_datadir}/git-core/templates/hooks/*.sample
%dir %{_datadir}/git-core/templates/info
%{_datadir}/git-core/templates/info/exclude
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
%doc %{_mandir}/man1/git-http-backend.1*
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
%doc %{_mandir}/man1/git-notes.1*
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
%doc %{_mandir}/man1/git-remote-helpers.1*
%doc %{_mandir}/man1/git-remote.1*
%doc %{_mandir}/man1/git-repack.1*
%doc %{_mandir}/man1/git-replace.1*
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
%doc %{_mandir}/man7/gitdiffcore.7*
%doc %{_mandir}/man7/gitglossary.7*
%doc %{_mandir}/man7/gitrevisions.7*
%doc %{_mandir}/man7/gittutorial-2.7*
%doc %{_mandir}/man7/gittutorial.7*
%doc %{_mandir}/man7/gitworkflows.7*


%files web
%defattr(-, root, root)
%doc README COPYING
%dir %{_datadir}/gitweb
%dir %{_datadir}/gitweb/static
%{_datadir}/gitweb/gitweb.cgi
%{_datadir}/gitweb/static/*.*


%files python
%defattr(-, root, root)
%doc README COPYING
%{python_sitelib}/git_remote_helpers*
%{_libexecdir}/git-core/git-remote-testgit


%files perl
%defattr(-, root, root)
%doc README COPYING
%{perl_sitelib}/Git.pm
%{perl_sitelib}/Error.pm
%doc %{_mandir}/man3/Git.3pm*
%doc %{_mandir}/man3/private-Error.3pm*


%files cvs
%defattr(-, root, root)
%doc README COPYING Documentation/*cvs*.txt
%{_bindir}/git-cvsserver
%{_libexecdir}/git-core/git-cvsexportcommit
%{_libexecdir}/git-core/git-cvsimport
%{_libexecdir}/git-core/git-cvsserver
%doc %{_mandir}/man1/git-cvsserver.1*
%doc %{_mandir}/man7/gitcvs-migration.7*


%files svn
%defattr(-, root, root)
%doc README COPYING Documentation/*svn*.txt
%{_libexecdir}/git-core/git-svn
