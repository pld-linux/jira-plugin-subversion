%define		plugin	subversion
%include	/usr/lib/rpm/macros.java
Summary:	JIRA Subversion plugin
Name:		jira-plugin-%{plugin}
Version:	0.10.5.2
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries/Java
Source0:	http://maven.atlassian.com/contrib/com/atlassian/jira/plugin/ext/subversion/atlassian-jira-subversion-plugin/%{version}/atlassian-jira-subversion-plugin-%{version}-distribution.zip
# Source0-md5:	5e220049093be0f732a174e7955aa13d
URL:		http://confluence.atlassian.com/display/JIRAEXT/JIRA+Subversion+plugin
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jira >= 4.1.1-2
Obsoletes:	jira-enterprise-plugin-subversion
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pluginsdir	%{_datadir}/jira/plugins
%define		pluginsdeploydir	%{_datadir}/jira/WEB-INF/lib

%description
A plugin to integrate JIRA with Subversion. This plugin displays
Subversion commit info in a tab on the associated JIRA issue. To link
a commit to a JIRA issue, the commit's text must contain the issue key
(eg. "This commit fixes TST-123").

%prep
%setup -q -n atlassian-jira-subversion-plugin-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{pluginsdeploydir},%{pluginsdir},%{_sysconfdir}/jira,%{_datadir}/jira/WEB-INF/classes}

cp subversion-jira-plugin.properties $RPM_BUILD_ROOT%{_sysconfdir}/jira/subversion-jira-plugin.properties
ln -s %{_sysconfdir}/jira/subversion-jira-plugin.properties $RPM_BUILD_ROOT%{_datadir}/jira/WEB-INF/classes/subversion-jira-plugin.properties

cp lib/*.jar $RPM_BUILD_ROOT%{pluginsdir}
cd lib
for I in *.jar; do
	ln -sf %{pluginsdir}/$I $RPM_BUILD_ROOT%{pluginsdeploydir}/$I
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,tomcat) %{_sysconfdir}/jira/subversion-jira-plugin.properties
%{_datadir}/jira/WEB-INF/classes/subversion-jira-plugin.properties
%{pluginsdir}/*.jar
%{pluginsdeploydir}/*.jar
