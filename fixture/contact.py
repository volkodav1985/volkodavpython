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
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.surname)
        self.change_field_value("company", contact.job)
        self.change_field_value("address", contact.mainaddress)
        self.change_field_value("mobile", contact.phone)
        self.change_field_value("byear", contact.year)
        self.change_field_value("address2", contact.secondaddress)



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
             self.contact_cache = []
             for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                 cells = element.find_elements_by_tag_name("td")
                 firstname = cells[2].text
                 lastname = cells[1].text
                 id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                 self.contact_cache.append(Contact(name=firstname, surname=lastname, id=id))
         return list(self.contact_cache)







