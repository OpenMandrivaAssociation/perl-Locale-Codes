%define upstream_name    Locale-Codes
%define upstream_version 3.27
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Standard language codes (such as ISO 639)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Locale/Locale-Codes-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(constant)

BuildArch:	noarch

%description
Locale::Codes is a distribution containing a set of modules. The modules
each deal with different types of codes which identify parts of the locale
including languages, countries, currency, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE META.yml ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.170.0-1mdv2011.0
+ Revision: 688750
- update to new version 3.17

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 3.160.0-2
+ Revision: 657445
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.160.0-1
+ Revision: 643399
- update to new version 3.16

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.150.0-2mdv2011.0
+ Revision: 612345
- fix description

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.150.0-1mdv2011.0
+ Revision: 612237
- update to new version 3.15

* Sat Nov 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.140.0-1mdv2011.0
+ Revision: 597080
- new version

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 3.130.0-3mdv2011.0
+ Revision: 562429
- rebuild

* Sat Jul 24 2010 Jérôme Quelin <jquelin@mandriva.org> 3.130.0-2mdv2011.0
+ Revision: 558164
- rebuild

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.130.0-1mdv2011.0
+ Revision: 551224
- update to 3.13

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 3.120.0-1mdv2010.1
+ Revision: 532136
- update to 3.12

* Tue Mar 02 2010 Jérôme Quelin <jquelin@mandriva.org> 3.110.0-1mdv2010.1
+ Revision: 513468
- update to 3.11

* Fri Feb 19 2010 Jérôme Quelin <jquelin@mandriva.org> 3.100.0-1mdv2010.1
+ Revision: 508047
- update to 3.10

* Thu Feb 11 2010 Jérôme Quelin <jquelin@mandriva.org> 3.0.0-1mdv2010.1
+ Revision: 504185
- import perl-Locale-Codes


* Thu Feb 11 2010 cpan2dist 3.00-1mdv
- initial mdv release, generated with cpan2dist


