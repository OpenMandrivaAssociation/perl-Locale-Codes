%define upstream_name    Locale-Codes
%define upstream_version 3.31
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Standard language codes (such as ISO 639)

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz

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
%doc README LICENSE META.yml 
%{_mandir}/man3/*
%{perl_vendorlib}/*



