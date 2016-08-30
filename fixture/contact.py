from model.contact import Contact


class ContactHelper:


    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("home").click()


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//form[@name='MainForm']/table[@id='maintable']//input[@name='selected[]']")[
            index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)



    def  edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        wd.find_elements_by_xpath("//form[@name='MainForm']/table[@id='maintable']//img[@title='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.home_page()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)




    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()



    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("secondaddress", contact.secondaddress)
        self.change_field_value("phone2", contact.secondphone)
        self.change_field_value("year", contact.year)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_contact_form(contact)
        self.enter_contact_create()
        self.home_page()
        self.contact_cache = None




    def enter_contact_create(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector('img[alt="Edit"]'))

    contact_cache = None

    def get_contact_list(self):
         if self.contact_cache is None:
             wd = self.app.wd
             self.app.open_home_page()
             self.contact_cache = []
             for row in wd.find_elements_by_name("entry"):
                 cells = row.find_elements_by_tag_name("td")
                 firstname = cells[1].text
                 lastname = cells[2].text
                 id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                 all_phones = cells[5].text.splitlines()
                 self.contact_cache.append(Contact(name=firstname, surname=lastname, id=id,
                                                   homephone=all_phones[0],mobilephone=all_phones[1],
                                                   workphone=all_phones[2], secondphone=all_phones[3]))
         return list(self.contact_cache)


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone=wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname = firstname, lastname = lastname,id = id,
                       homephone = homephone,workphone = workphone,
                       mobilephone = mobilephone,secondphone = secondphone)







