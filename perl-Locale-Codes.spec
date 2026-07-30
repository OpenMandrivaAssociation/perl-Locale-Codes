%define upstream_name    Locale-Codes
%define upstream_version 3.90
Name:		perl-%{upstream_name}
Version:	3.90
Release:	2

Summary:	Standard language codes (such as ISO 639)

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/SBECK-github/Locale-Codes
Source0:	https://cpan.metacpan.org/authors/id/S/SB/SBECK/Locale-Codes-3.90.tar.gz

BuildRequires:	make
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
%setup -q -n Locale-Codes-3.90

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc README LICENSE META.yml 
%{_mandir}/man3/*
%{perl_vendorlib}/*



