#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	ParseWords
Summary:	String::ParseWords - Parse a string into logical words
Summary(pl):	String::ParseWords - analiza �a�cucha z rozk�adem na logiczne s�owa
Name:		perl-String-ParseWords
Version:	0.1
Release:	2
License:	IBM Public License Version 1.0
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::ParseWords is designed to parse logical words from a string.
Logical words are defined as sets of characters between double quotes
or sets of characters between whitespace.

%description -l pl
Modu� String::ParseWords s�u�y do analizy logicznych s��w w �a�cuchu.
Logiczne s�owa s� zdefiniowane jako zbiory znak�w mi�dzy podw�jnymi
cudzys�owami lub zbiory znakow mi�dzy bia�ymi znakami (odst�pami).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
