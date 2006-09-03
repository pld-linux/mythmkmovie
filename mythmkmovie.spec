Summary:	An archiving assistant for MythTV
Name:		mythmkmovie
Version:	1.1.4
Release:	0.5
License:	GPL2
Group:		Applications/Multimedia
URL:		http://www.icelus.org/
Source0:	http://www.icelus.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	fdff9695f8c1d5df6f4f691123097d26
BuildRequires:	libpng-devel
BuildRequires:	perl-Curses
BuildRequires:	perl-DBD-mysql
BuildRequires:	perl-DBI
BuildRequires:	sed >= 4.0
Requires:	libpng
Requires:	mencoder
Requires:	mythtv
Requires:	perl-Curses
Requires:	perl-DBD-MySQL
Requires:	perl-DBI
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MythMkMovie is an archiving assistant for use with MythTV. It will
produce a DiVX file for your viewing/archiving pleasure, and remove
the commercials in the process (IF you've gone through and removed
them when watching it in MythTV). It can be drivien from the command
line, or it also has a curses based interface to allow you to navigate
the files you have stored on your computer.

%prep
%setup -q
%{__sed} -i -e 's|%{_prefix}/local|'%{_prefix}'|g' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/mkmovie/.packlist
[ -s $RPM_BUILD_ROOT%{perl_vendorarch}/auto/mkmovie/mkmovie.bs ] || \
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/mkmovie/mkmovie.bs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mkmovie
%attr(755,root,root) %{_bindir}/mythframes
%attr(755,root,root) %{perl_vendorarch}/auto/mkmovie/mkmovie.so
%{_mandir}/man1/mkmovie.1*
%{_mandir}/man1/mythframes.1*
