%define		database_version	20080416
%define		rel	2
Summary:	Scam database for clamav
Name:		clamav-database-scam
Version:	0.1
Release:	%{database_version}.%{rel}
License:	GPL
Group:		Applications/Databases
Source0:	 http://www.sanesecurity.com/clamav/scamsigs/scam.ndb.gz
# Source0-md5:	73beea066a50d248c5bf01e2bad02b85
URL:		http://www.sanesecurity.co.uk/clamav/
Requires:	clamav
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scam database for ClamAV which will help detect some types of stock, lottery,
419 and some image spams that are around at the moment. (Updated
%{database_version}).

%prep
%setup -qcT
%{__gzip} -dc %{SOURCE0} > $(basename %{SOURCE0} .gz)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/clamav
install *.ndb $RPM_BUILD_ROOT/var/lib/clamav

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(644,clamav,root) %verify(not md5 mtime size) /var/lib/clamav/*.ndb
