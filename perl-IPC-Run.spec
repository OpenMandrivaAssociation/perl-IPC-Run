%define modname	IPC-Run
%define modver	0.91

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IPC/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%prep
%setup -qn %{modname}-%{modver}
chmod 644 Changes
chmod 755 eg/*
perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' eg/*

rm -f lib/IPC/Run/Win32Helper.pm \
      lib/IPC/Run/Win32IO.pm \
      lib/IPC/Run/Win32Pump.pm

sed -i -e '/Win32Helper.pm/d;/Win32IO.pm/d;/Win32Pump.pm/d' MANIFEST

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%make test

%install
%makeinstall_std

%files
%doc Changes TODO eg
%{perl_vendorlib}/IPC
%{_mandir}/man3/*

