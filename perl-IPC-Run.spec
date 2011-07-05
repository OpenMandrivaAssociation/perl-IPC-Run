%define upstream_name	 IPC-Run
%define upstream_version 0.90

%define _requires_exceptions Win32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
