#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from core.interface import print_line
from core.components_helper.components_helper import ComponentsHelper
from core.webapi import WebAPI


class SetHelper(object):

    def __init__(self):
        self.web_api = WebAPI()
        self.components_helper = ComponentsHelper()

    def create_set_validate(self, api_data: dict) -> bool:
        if api_data['platform'] is None:
            print_line('Empty Platform name. Please use --platform=platform_name parameter.')
            return False

        platforms = self.get_my_platforms(api_data=api_data)

        if api_data['platform'] not in platforms:
            print_line(f"Platform {api_data['platform']} does not exists.")
            return False

        if api_data['project'] is None:
            print_line('Empty Project name. Please use --project=project_name parameter.')
            return False

        projects = self.get_my_projects(api_data=api_data)

        if api_data['project'] not in projects:
            print_line(f"Project {api_data['project']} does not exists.")
            return False

        set_name = api_data['set']
        current_set_name = self.components_helper.get_current_set_name(api_data=api_data)[0]

        if current_set_name == set_name:
            print_line(f'Current set with name {set_name} already exists.')
            print_line('Please, use another name, or use no --set parameter to autoincrement set name.')
            return False

        if set_name is None:
            if current_set_name[-1].isdigit():
                d = int(current_set_name[-1])
                d = d + 1
                current_set_name = current_set_name[:-1]
                set_name = current_set_name + str(d)

            else:
                set_name = current_set_name + '.1'

        api_data['set'] = set_name

        return True

    # Target = OS packages

    def create_set_os_auto_system_none(self, api_data: dict) -> bool:
        """
        Create Component Set with OS packages, collected by shell command.
        :param api_data: api data set
        :return: result
        """
        api_data['components'] = self.components_helper.get_components_os_auto_system_none(api_data=api_data)

        if api_data['components'] [0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_os_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with OS packages, collected from shell command
        and stored in file, defined in path.
        :param api_data: api data set
        :return: result
        """
        api_data['components'] = self.components_helper.get_components_os_auto_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    # Target = Python packages

    def create_set_pip_auto_system_none(self, api_data: dict) -> bool:
        """
        Create Component Set with Python PIP packages, collected from shell command.
        :param api_data:
        :return:
        """
        api_data['components'] = self.components_helper.get_components_pip_auto_system_none()

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_pip_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with Python PIP packages, collected from shell command
        and stored in file, defined in path.
        :param api_data: api data set
        :return: result
        """
        api_data['components'] = self.components_helper.get_components_pip_auto_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_requirements_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with Python requirements.txt file, defined in path.
        :param api_data: spi data set
        :return: result
        """
        api_data['components'] = self.components_helper.get_components_requirements_auto_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_npm_auto_system_none(self, api_data: dict) -> bool:
        """
        Create Component Set with NPM packages, collected from shell command (nmp list --json).
        Shell command runs global from root path.
        :param api_data:
        :return:
        """
        api_data['components'] = self.components_helper.get_components_npm_auto_system_none(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_npm_local_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with NPM packages, collected from shell command (npm list --json).
        Shell command runs local from path, defined by --file parameter.
        :param api_data:
        :return:
        """
        api_data['components'] = self.components_helper.get_components_npm_local_auto_system_none(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_npm_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with NPM packages, collected from shell command (npm list --json)
        and stored in file, defined in path.
        :param api_data: api data set
        :return: result
        """
        api_data['components'] = self.components_helper.get_components_npm_auto_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_package_json_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with NPM packages from package.json, defined by --file parameter.
        :param api_data: api data set
        :return: result
        """
        api_data['components'] = self.components_helper.get_components_package_json_auto_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_package_lock_json_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with NPM packages from package-lock.json, defined by --file parameter.
        :param api_data:
        :return:
        """
        api_data['components'] = self.components_helper.get_components_npm_lock_auto_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_gem_auto_system_none(self, api_data: dict) -> bool:
        """
        Create Component Set with Ruby packages, collected from shell command.
        :param api_data:
        :return:
        """
        api_data['components'] = self.components_helper.get_components_gem_auto_system_none(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_gem_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with Ruby packages, collected from shell command and
        stored in gem list file, defined in --file parameter.
        :param api_data:
        :return:
        """
        api_data['components'] = self.components_helper.get_components_gem_auto_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_gemfile_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with Ruby packages, collected from Gemfile, defined
        by --file parameter.
        :param api_data:
        :return:
        """
        api_data['components'] = self.components_helper.get_components_gemfile_auto_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_gemfile_lock_auto_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with Ruby packages, collected from Gemfile.lock file,
        defined by --file parameter.
        :param api_data:
        :return:
        """
        api_data['components'] = self.components_helper.get_components_gemfile_lock_auto_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_any_auto_user_path(self, api_data: dict) -> bool:
        """
        Create Component Set with different packages, collected in file,
        defined by path with simple multiline format: name=version…
        :param api_data:
        :return:
        """
        api_data['components'] = self.components_helper.get_components_any_auto_user_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_any_manual_user_none(self, api_data: dict) -> bool:
        """
        Create Component Set with different packages, asked in interactive mode.
        :param api_data: api data set
        :return: result
        """
        api_data['components'] = self.components_helper.get_components_any_manual_user_none()

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_php_composer_json_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with packages from PHP Composer.json file.
        :param api_data: api data set
        :return: result
        """
        api_data['components'] = self.components_helper.get_components_php_composer_json_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    def create_set_php_composer_lock_system_path(self, api_data: dict) -> bool:
        """
        Create Component Set with packages from PHP Composer.lock file.
        :param api_data: api data set
        :return: result
        """
        api_data['components'] = self.components_helper.get_components_php_composer_lock_system_path(api_data=api_data)

        if api_data['components'][0] is None:
            return False

        api_data['platform_number'] = self.web_api.get_platform_number_by_name(api_data=api_data)
        if api_data['platform_number'] == -1:
            print_line(f"No such platform: {api_data['platform']}")
            return False

        api_data['project_number'] = self.web_api.get_project_number_by_name(api_data=api_data)
        if api_data['project_number'] == -1:
            print_line(f"No such project: {api_data['project']}")
            return False

        api_data['project_url'] = api_data['organization']['platforms'][api_data['platform_number']]['projects'][api_data['project_number']]['url']

        return self.web_api.send_create_new_component_set_request(api_data=api_data)

    @staticmethod
    def get_my_platforms(api_data: dict) -> list:
        """
        Get platforms names as list.
        :param api_data: api data set
        :return: result
        """

        if api_data['organization'] is None:
            return []

        if api_data['organization']['platforms'] is None:
            return []

        platforms = []
        for platform in api_data['organization']['platforms']:
            platforms.append(platform['name'])

        return platforms

    def get_my_projects(self, api_data: dict) -> list:
        """
        Get projects names as list.
        :param api_data: api data set
        :return: result
        """

        if api_data['organization'] is None:
            return []

        if api_data['organization']['platforms'] is None:
            return []

        platform_number = self.web_api.get_platform_number_by_name(api_data=api_data)

        if platform_number == -1:
            return []

        projects = []
        for project in api_data['organization']['platforms'][platform_number]['projects']:
            projects.append(project['name'])

        return projects