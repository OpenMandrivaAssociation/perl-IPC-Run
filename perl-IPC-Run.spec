%define module	IPC-Run
%define name	perl-%{module}
%define version 0.84
%define release %mkrel 1
%define _requires_exceptions Win32

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IPC/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%prep
%setup -q -n %{module}-%{version}
chmod 644 Changes
chmod 755 eg/*
perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' eg/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes TODO eg
%{perl_vendorlib}/IPC
%{_mandir}/*/*

