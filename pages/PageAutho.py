from pages.Locators import LocatorsProject
from pages.BaseApp import BasePage


class RegPage(BasePage):
    """Регистрация [REG]"""

    # Ввод значений и нажатие кнопок:
    def btn_click_enter(self):
        btn_enter = self.find_elements(LocatorsProject.REG_bfENTER)[0].click()  # +S
        return btn_enter

    def btn_click_way(self):
        btn_way = self.find_element(LocatorsProject.REG_bWAY).click()
        return btn_way

    def btn_click_email(self):
        btn_email = self.find_element(LocatorsProject.REG_bEMAIL).click()
        return btn_email

    def enter_email(self, value):
        val_email = self.find_element(LocatorsProject.REG_vEMAIL).send_keys(value)
        return val_email

    def btn_click_getcode(self):
        btn_get_code = self.find_element(LocatorsProject.REG_bGET_CODE).click()
        return btn_get_code

    def enter_code(self, value):
        val_code = self.find_elements(LocatorsProject.REG_vCODE)[0].send_keys(value)  # +S
        return val_code

    def find_elem_inputcode(self):
        find_inputcode = self.find_element(LocatorsProject.REG_fINPUTCODE)
        return find_inputcode

    # Для клика по элементу используем JS в тест-файле!
    def btn_click_user(self):
        btn_user = self.find_element(LocatorsProject.REG_bUSER)
        return btn_user

    def btn_click_changepass(self):
        btn_change_pass = self.find_element(LocatorsProject.REG_bCHANGE_PASS).click()
        return btn_change_pass

    def enter_pass(self, value):
        val_passw = self.find_element(LocatorsProject.REG_vPASS).send_keys(value)
        return val_passw

    def enter_pass2(self, value):
        val_passw2 = self.find_element(LocatorsProject.REG_vPASS2).send_keys(value)
        return val_passw2

    def btn_click_save(self):
        btn_save = self.find_element(LocatorsProject.REG_bSAVE).click()
        return btn_save

    def btn_click_exit(self):
        btn_exit = self.find_element(LocatorsProject.REG_bEXIT).click()
        return btn_exit

    def find_elem_enter(self):
        find_enter = self.find_elements(LocatorsProject.REG_bfENTER)[0]  # +S
        return find_enter


class AuthPage(BasePage):
    """Авторизация [AUTH]"""

    # Ввод значений и нажатие кнопок:
    def btn_click_enter(self):
        btn_enter = self.find_elements(LocatorsProject.REG_bfENTER)[0].click()  # +S
        return btn_enter

    def btn_click_way(self):
        btn_way = self.find_element(LocatorsProject.REG_bWAY).click()
        return btn_way

    def btn_click_bypass(self):
        btn_bypass = self.find_element(LocatorsProject.AUTH_bBYPASS).click()
        return btn_bypass

    def enter_email(self, value):
        val_email = self.find_element(LocatorsProject.REG_vEMAIL).send_keys(value)
        return val_email

    def enter_pass(self, value):
        val_passw = self.find_element(LocatorsProject.AUTH_vPASS).send_keys(value)
        return val_passw

    def btn_click_login(self):
        btn_login = self.find_element(LocatorsProject.AUTH_bLOGIN).click()
        return btn_login

    def find_elem_errorpass(self):
        find_errorpass = self.find_element(LocatorsProject.AUTH_fERRORPASS)
        return find_errorpass

    # Для клика по элементу используем JS в тест-файле!
    def btn_click_user(self):
        btn_user = self.find_element(LocatorsProject.REG_bUSER)
        return btn_user


class MainPage(BasePage):
    """Главная страница сайта [MPAGE]"""

    def find_elem_rows(self):
        find_page_rows = self.find_elements(LocatorsProject.MPAGE_fROW)  # +S
        return find_page_rows

    def btn_click_catalog(self):
        btn_catalog = self.find_element(LocatorsProject.GOOD_bCATALOG).click()
        return btn_catalog

    def find_elem_tv(self):
        find_menu_tv = self.find_element(LocatorsProject.MPAGE_fTV)
        return find_menu_tv

    def btn_click_close(self):
        btn_close = self.find_element(LocatorsProject.MPAGE_bCLOSE).click()
        return btn_close

    def not_find_elem_tv(self):
        notfind_menu_tv = self.not_find_element(LocatorsProject.MPAGE_fTV)
        return notfind_menu_tv

    def find_elem_smartphones(self):
        find_smartphones = self.find_element(LocatorsProject.GOOD_fSMARTPHONES)
        return find_smartphones

    def find_elem_samsung(self):
        find_samsung = self.find_elements(LocatorsProject.GOOD_fSAMSUNG)[1]  # +S
        return find_samsung

    def find_elem_smartphonprod(self):
        find_smartphonprod = self.find_elements(LocatorsProject.GOOD_fSMARTPHONPROD)[1]  # +S
        return find_smartphonprod

    def find_elem_receivers(self):
        find_receivers = self.find_element(LocatorsProject.MPAGE_fRECEIVERS)
        return find_receivers

    def find_elem_audio(self):
        find_audio = self.find_element(LocatorsProject.MPAGE_fAUDIO)
        return find_audio

    def find_elem_atechniq(self):
        find_atechniq = self.find_element(LocatorsProject.MPAGE_fATECHNIQUE)
        return find_atechniq

    def find_elem_comptech(self):
        find_comptech = self.find_element(LocatorsProject.MPAGE_bfCOMPTECH)
        return find_comptech

    def find_elem_lcdmonitor(self):
        find_lcdmonitor = self.find_element(LocatorsProject.MPAGE_fLCDMONITOR)
        return find_lcdmonitor

    def find_elem_computers(self):
        find_computers = self.find_elements(LocatorsProject.MPAGE_fCOMPUTER)[1]  # +S
        return find_computers

    def find_elem_fridges(self):
        find_fridges = self.find_element(LocatorsProject.GOOD_fFRIDGES)
        return find_fridges

    def find_elem_freezers(self):
        find_freezers = self.find_elements(LocatorsProject.GOOD_fFREEZERS)[0]  # +S
        return find_freezers

    def find_elem_washers(self):
        find_washers = self.find_element(LocatorsProject.MPAGE_bfWASHERS)
        return find_washers

    def find_elem_dryauto(self):
        find_dryauto = self.find_element(LocatorsProject.MPAGE_fDRYAUTO)
        return find_dryauto

    def find_elem_allwashers(self):
        find_allwashers = self.find_elements(LocatorsProject.MPAGE_bfALLWASHERS)[5]  # +S
        return find_allwashers

    def find_elem_builtin(self):
        find_builtin = self.find_element(LocatorsProject.MPAGE_bfBUILTIN)
        return find_builtin

    def find_elem_winecase(self):
        find_winecase = self.find_elements(LocatorsProject.MPAGE_fWINECASE)[1]  # +S
        return find_winecase

    def find_elem_diswashers(self):
        find_diswashers = self.find_element(LocatorsProject.MPAGE_bfDISWASHERS)
        return find_diswashers

    def find_elem_compwashers(self):
        find_compwashers = self.find_element(LocatorsProject.MPAGE_fCOMPWASHERS)
        return find_compwashers

    def find_elem_stoves(self):
        find_stoves = self.find_element(LocatorsProject.MPAGE_bfSTOVES)
        return find_stoves

    def find_elem_gascookers(self):
        find_gascookers = self.find_elements(LocatorsProject.MPAGE_fGASCOOKERS)[0]  # +S
        return find_gascookers

    def find_elem_forkitchen(self):
        find_forkitchen = self.find_element(LocatorsProject.MPAGE_bfFORKITCHEN)
        return find_forkitchen

    def find_elem_coffeeset(self):
        find_coffeeset = self.find_element(LocatorsProject.MPAGE_fCOFFEESET)
        return find_coffeeset

    def find_elem_domestic(self):
        find_domestic = self.find_element(LocatorsProject.MPAGE_bfDOMESTIC)
        return find_domestic

    def find_elem_smarthouse(self):
        find_smarthouse = self.find_element(LocatorsProject.MPAGE_fSMARTHOUSE)
        return find_smarthouse

    def find_elem_beauty(self):
        find_beauty = self.find_element(LocatorsProject.MPAGE_bfBEAUTY)
        return find_beauty

    def find_elem_hairdriers(self):
        find_hairdriers = self.find_element(LocatorsProject.MPAGE_fHAIRDRIERS)
        return find_hairdriers

    def find_elem_climatic(self):
        find_climatic = self.find_element(LocatorsProject.MPAGE_bfCLIMATIC)
        return find_climatic

    def find_elem_fireplaces(self):
        find_fireplaces = self.find_element(LocatorsProject.MPAGE_fFIREPLACES)
        return find_fireplaces

    def find_elem_construction(self):
        find_construction = self.find_element(LocatorsProject.MPAGE_bfCONSTRUCTION)
        return find_construction

    def find_elem_perforators(self):
        find_perforators = self.find_element(LocatorsProject.MPAGE_fPERFORATORS)
        return find_perforators

    def find_elem_cottagegard(self):
        find_cottagegard = self.find_element(LocatorsProject.MPAGE_bfCOTTAGEGARD)
        return find_cottagegard

    def find_elem_furniture(self):
        find_furniture = self.find_element(LocatorsProject.MPAGE_fFURNITURE)
        return find_furniture

    def find_elem_sportgoods(self):
        find_sportgoods = self.find_element(LocatorsProject.MPAGE_bfSPORTGOODS)
        return find_sportgoods

    def find_elem_strongfitness(self):
        find_strongfitness = self.find_element(LocatorsProject.MPAGE_fSTRONGFITNESS)
        return find_strongfitness

    def find_elem_kids(self):
        find_kids = self.find_element(LocatorsProject.MPAGE_bfKIDS)
        return find_kids

    def find_elem_constructors(self):
        find_constructors = self.find_element(LocatorsProject.MPAGE_fCONSTRUCTORS)
        return find_constructors

    def find_elem_discounted(self):
        find_discounted = self.find_element(LocatorsProject.MPAGE_bfDISCOUNTED)
        return find_discounted

    def find_elem_discountfirst(self):
        find_discountfirst = self.find_elements(LocatorsProject.MPAGE_fDISCOUNTFIRST)[0]  # +S
        return find_discountfirst

    def find_elem_discountsecond(self):
        find_discountsecond = self.find_elements(LocatorsProject.MPAGE_bfDISCOUNTSECOND)[0]  # +S
        return find_discountsecond

    def find_elem_discountback(self):
        find_discback = self.find_element(LocatorsProject.MPAGE_bfDISCOUNTBACK)
        return find_discback

    def find_elem_alldiscount(self):
        find_alldiscount = self.find_elements(LocatorsProject.MPAGE_fALLDISCOUNTGOODS)  # +S
        return find_alldiscount

    def find_elem_discountproducts(self):
        find_discountproducts = self.find_elements(LocatorsProject.MPAGE_fDISCOUNTPRODUCTS)  # +S
        return find_discountproducts

    def find_elem_productname(self):
        find_productname = self.find_element(LocatorsProject.MPAGE_fPRODUCTNAME)
        return find_productname

    def find_elem_productsname(self):
        find_productsname = self.find_elements(LocatorsProject.MPAGE_fPRODUCTNAME)  # +S
        return find_productsname

    def find_elem_productimage(self):
        find_productimage = self.find_element(LocatorsProject.MPAGE_fPRODUCTIMAGE)
        return find_productimage

    def find_elem_reasonmarkdown(self):
        find_reasonmarkdown = self.find_elements(LocatorsProject.MPAGE_fREASONMARKDOWN)[2]  # +S
        return find_reasonmarkdown

    def find_elem_productprice(self):
        find_productprice = self.find_elements(LocatorsProject.MPAGE_fPRODUCTPRICE)[0]  # +S
        return find_productprice

    def find_elem_oldprice(self):
        find_oldprice = self.find_elements(LocatorsProject.MPAGE_fOLDPRICE)[0]  # +S
        return find_oldprice

    def find_elem_action(self):
        find_action = self.find_element(LocatorsProject.MPAGE_bfACTION)
        return find_action

    def find_elem_brandaction(self):
        find_brandaction = self.find_elements(LocatorsProject.MPAGE_bfBRANDACTION)  # +S
        return find_brandaction

    def find_elem_brands(self):
        find_brands = self.find_element(LocatorsProject.MPAGE_bfBRANDS)
        return find_brands

    def btn_click_scrollup(self):
        btn_scrollup = self.find_element(LocatorsProject.MPAGE_bfSCROLLUP)
        return btn_scrollup

    def not_find_element_scrollup(self):
        find_noscrollup = self.find_element(LocatorsProject.MPAGE_bfNOSCROLLUP)
        return find_noscrollup

    def find_elem_header(self):
        find_header = self.find_elements(LocatorsProject.MPAGE_fHEADER)  # +S
        return find_header

    def btn_click_logoimage(self):
        btn_logoimage = self.find_element(LocatorsProject.MPAGE_bLOGOIMAGE).click()
        return btn_logoimage

    def btn_click_body(self):
        btn_body = self.find_elements(LocatorsProject.MPAGE_bfBODY)  # +S
        return btn_body

    def btn_goodday(self):
        btn_goodday = self.find_element(LocatorsProject.MPAGE_bfGOODDAY).click()
        return btn_goodday

    def find_elem_gooddayname(self):
        find_gooddayname = self.find_element(LocatorsProject.MPAGE_fGOODDAYNAME)
        return find_gooddayname

    def find_elem_footer(self):
        find_footer = self.find_elements(LocatorsProject.MPAGE_fFOOTER)  # +S
        return find_footer

    def btn_click_favorites(self):
        btn_favorites = self.find_elements(LocatorsProject.MPAGE_bFAVORITES)[1]  # +S
        return btn_favorites

    def find_elem_favoritcounter(self):
        find_favoritcounter = self.find_element(LocatorsProject.MPAGE_bFAVORITESCOUNT)
        return find_favoritcounter

    def btn_click_network(self):
        btn_network = self.find_elements(LocatorsProject.MPAGE_bNETWORK)
        return btn_network

    def btn_click_town(self):
        btn_town = self.find_element(LocatorsProject.MPAGE_bTOWN)
        return btn_town

    def btn_click_townkazan(self):
        btn_townkazan = self.find_element(LocatorsProject.MPAGE_bTOWNKAZAN).click()
        return btn_townkazan


class SearchField(BasePage):
    """Поле для поиска [SEARCH]"""

    def find_elem_field(self, value):
        find_field = self.find_element(LocatorsProject.SEARCH_vFIELD).send_keys(value)
        return find_field

    def btn_search(self):
        btn_search = self.find_element(LocatorsProject.SEARCH_bSEARCH).click()
        return btn_search

    def find_elem_byname(self):
        find_byname = self.find_elements(LocatorsProject.SEARCH_fBYNAME)[2]  # +S
        return find_byname

    def find_elem_amountfound(self):
        find_amountfound = self.find_element(LocatorsProject.SEARCH_fAMOUNTFOUND)
        return find_amountfound

    def find_elem_comentfound(self):
        find_comentfound = self.find_element(LocatorsProject.SEARCH_fCOMENTFOUND)
        return find_comentfound

    def find_elem_bycode(self):
        find_bycode = self.find_elements(LocatorsProject.SEARCH_fBYCODE)[1]  # +S
        return find_bycode


class GoodsCounter(BasePage):
    """СчётчикТоваров [GOOD]"""

    def btn_click_catalog(self):
        btn_catalog = self.find_element(LocatorsProject.GOOD_bCATALOG).click()
        return btn_catalog

    def find_elem_fridges(self):
        find_fridges = self.find_element(LocatorsProject.GOOD_fFRIDGES)
        return find_fridges

    def find_elem_freezers(self):
        find_freezers = self.find_elements(LocatorsProject.GOOD_fFREEZERS)[0]  # +S
        return find_freezers

    def find_elem_counter(self):
        find_counter = self.find_element(LocatorsProject.GOOD_fCOUNTER)
        return find_counter

    def find_elem_goods_name(self):
        find_goods_name = self.find_element(LocatorsProject.GOOD_fGOODSNAME)
        return find_goods_name

    def find_elem_goods_price(self):
        find_goods_price = self.find_elements(LocatorsProject.GOOD_fGOODSPRICE)  # +S
        return find_goods_price

    def find_elem_page_link(self):
        find_page_link = self.find_elements(LocatorsProject.GOOD_fPAGELINK)  # +S
        return find_page_link


class FilterSort(BasePage):
    """Фильтр и Сортировка [FTRS]"""

    def btn_click_advertis(self):
        btn_advertis = self.find_element(LocatorsProject.FTRS_bADVERTIS).click()
        return btn_advertis

    def find_elem_pricemarkd(self):
        find_pricemarkd = self.find_elements(LocatorsProject.FTRS_fPRICEMARKD)  # +S
        return find_pricemarkd

    def find_price_priceall(self):
        find_priceall = self.find_elements(LocatorsProject.FTRS_fPRICEALL)  # +S
        return find_priceall

    def find_price_markdown(self):
        find_markdown = self.find_elements(LocatorsProject.FTRS_fMARKDOWN)  # +S
        return find_markdown

    def find_elem_price(self):
        find_price = self.find_elements(LocatorsProject.FTRS_fPRICE)  # +S
        return find_price

    def find_elem_minprice(self):
        find_minprice = self.find_element(LocatorsProject.FTRS_vMINPRICE)
        return find_minprice

    def find_elem_maxprice(self):
        find_maxprice = self.find_element(LocatorsProject.FTRS_vMAXPRICE)
        return find_maxprice

    def btn_click_show(self):
        btn_show = self.find_element(LocatorsProject.FTRS_bSHOW).click()
        return btn_show

    def btn_click_clear(self):
        btn_clear = self.find_element(LocatorsProject.FTRS_bCLEAR).click()
        return btn_clear

    def btn_click_prodacer(self):
        btn_prodacer = self.find_element(LocatorsProject.FTRS_bPROD_ACER)
        return btn_prodacer

    def btn_click_prodlenovo(self):
        btn_prodlenovo = self.find_element(LocatorsProject.FTRS_bPROD_LENOVO)
        return btn_prodlenovo

    def find_elem_nameproduct(self):
        find_nameproduct = self.find_elements(LocatorsProject.SEARCH_fBYNAME)  # +S
        return find_nameproduct

    def btn_click_opersystem(self):
        btn_opersystem = self.find_element(LocatorsProject.FTRS_bOPERSYSTEM)
        return btn_opersystem

    def btn_click_osdos(self):
        btn_osdos = self.find_element(LocatorsProject.FTRS_bOS_DOS)
        return btn_osdos

    def btn_click_oswindows(self):
        btn_oswindows = self.find_element(LocatorsProject.FTRS_bOS_WINDOWS)
        return btn_oswindows

    def find_elem_findosproduct(self):
        find_findosproduct = self.find_elements(LocatorsProject.FTRS_fFIND_OS)  # +S
        return find_findosproduct

    def btn_click_sorting(self):
        btn_sorting = self.find_element(LocatorsProject.FTRS_bSORTING).click()
        return btn_sorting

    def btn_click_sortcheap(self):
        btn_sortcheap = self.find_element(LocatorsProject.FTRS_bSORTCHEAP).click()
        return btn_sortcheap

    def btn_click_sortexpensive(self):
        btn_sortexpensive = self.find_element(LocatorsProject.FTRS_bSORTEXPENS).click()
        return btn_sortexpensive

    def btn_click_notavailable(self):
        btn_notavailable = self.find_element(LocatorsProject.FTRS_bNOTAVAILABLE)
        return btn_notavailable

    def find_elem_statusavailable(self):
        find_statusavailable = self.find_elements(LocatorsProject.FTRS_fSTATUSAVAILABLE)  # +S
        return find_statusavailable


class ProductCardBasket(BasePage):
    """Карточка товара и Корзина [PCB]"""

    def find_elem_productsname(self):
        find_productsname = self.find_elements(LocatorsProject.MPAGE_fPRODUCTNAME)  # +S
        return find_productsname

    def find_elem_locateimages(self):
        find_locateimages = self.find_elements(LocatorsProject.PCB_fLOCATEIMAGES)  # +S
        return find_locateimages

    def find_elem_cardbycode(self):
        find_cardbycode = self.find_elements(LocatorsProject.SEARCH_fBYCODE)  # +S
        return find_cardbycode

    def find_elem_description(self):
        find_description = self.find_elements(LocatorsProject.PCB_fDESCRIPTION)  # +S
        return find_description

    def find_elem_baskets(self):
        find_baskets = self.find_elements(LocatorsProject.PCB_fBASKET)[0]  # +S
        return find_baskets

    def find_elem_basketsforcard(self):
        find_basketsforcard = self.find_elements(LocatorsProject.PCB_fBASKET)  # +S
        return find_basketsforcard

    def find_elem_basketnum(self):
        find_basketnum = self.find_element(LocatorsProject.PCB_fBASKETNUM)
        return find_basketnum

    def btn_click_inbasket(self):
        btn_inbasket = self.find_element(LocatorsProject.PCB_bINBASKET)
        return btn_inbasket

    def btn_click_inbasket2(self):
        btn_inbasket2 = self.find_element(LocatorsProject.PCB_bINBASKET2)
        return btn_inbasket2

    def find_elem_basketnamegoods(self):
        find_basketnamegoods = self.find_elements(LocatorsProject.PCB_fBASKETNAMEGOODS)[0]  # +S
        return find_basketnamegoods

    def find_elem_firstproductname(self):
        find_firstproductname = self.find_elements(LocatorsProject.MPAGE_fPRODUCTNAME)[0]  # +S
        return find_firstproductname

    def btn_click_basket(self):
        btn_basket = self.find_element(LocatorsProject.PCB_bBASKET)
        return btn_basket

    def btn_click_delfrombasket(self):
        btn_delfrombasket = self.find_element(LocatorsProject.PCB_bDELFROMBASKET).click()
        return btn_delfrombasket

    def btn_click_delfrombasketyes(self):
        btn_delfrombasketyes = self.find_elements(LocatorsProject.PCB_bDELFROMBASKETYES)[1].click()
        return btn_delfrombasketyes

    def find_elem_basketempty(self):
        find_basketempty = self.find_element(LocatorsProject.PCB_fBASKETEMPTY)
        return find_basketempty

    def btn_click_goshopping(self):
        btn_goshopping = self.find_element(LocatorsProject.PCB_bGOSHOPPING)
        return btn_goshopping

    def btn_click_clearbasket(self):
        btn_clearbasket = self.find_element(LocatorsProject.PCB_bCLEARBASKET).click()
        return btn_clearbasket

    def find_elem_baskets_third(self):
        find_baskets_third = self.find_elements(LocatorsProject.PCB_fBASKET)[2]  # +S
        return find_baskets_third

    def btn_click_baskets_some(self):
        btn_baskets_some = self.find_elements(LocatorsProject.PCB_fBASKET)  # +S
        return btn_baskets_some

    # Число индекса [3] зависит от кол-ва товаров в корзине. При трёх товарах, индекс на кнопку удаления = 3.
    def btn_click_delfrombasketclear(self):
        btn_delfrombasketclear = self.find_elements(LocatorsProject.PCB_bDELFROMBASKETYES)[3].click()
        return btn_delfrombasketclear

    def btn_click_insurance(self):
        btn_insurance = self.find_element(LocatorsProject.PCB_bINSURANCE).click()
        return btn_insurance

    def btn_click_nohassle(self):
        btn_nohassle = self.find_elements(LocatorsProject.PCB_bNOHASSLE)[1].click()  # +S
        return btn_nohassle

    def btn_click_addorder(self):
        btn_addorder = self.find_element(LocatorsProject.PCB_bADDORDER).click()
        return btn_addorder

    def find_elem_nohassleok(self):
        find_nohassleok = self.find_element(LocatorsProject.PCB_fNOHASSLEOK)
        return find_nohassleok

    def find_elem_totalprice(self):
        find_totalprice = self.find_elements(LocatorsProject.PCB_fTOTALPRICE)[1]  # +S
        return find_totalprice

    def btn_click_basketcheckout(self):
        btn_basketcheckout = self.find_elements(LocatorsProject.PCB_bBASKETCHECKOUT)[0].click()  # +S
        return btn_basketcheckout

    def elem_click_basketphone(self):
        elem_basketphone = self.find_element(LocatorsProject.PCB_fBASKETPHONE).click()
        return elem_basketphone

    def find_elem_basketphone(self, value):
        find_basketphone = self.find_element(LocatorsProject.PCB_vBASKETPHONEIN).send_keys(value)
        return find_basketphone

    def elem_click_basketemail(self):
        elem_basketemail = self.find_element(LocatorsProject.PCB_fBASKETEMAIL).click()
        return elem_basketemail

    def find_elem_basketemail(self, value):
        find_basketemail = self.find_element(LocatorsProject.PCB_vBASKETEMAILIN).send_keys(value)
        return find_basketemail

    def elem_click_basketsurname(self):
        elem_basketsurname = self.find_element(LocatorsProject.PCB_fBASKETSURNAME).click()
        return elem_basketsurname

    def find_elem_basketsurname(self, value):
        find_basketsurname = self.find_element(LocatorsProject.PCB_vBASKETSURNAMEIN).send_keys(value)
        return find_basketsurname

    def elem_click_basketname(self):
        elem_basketname = self.find_element(LocatorsProject.PCB_fBASKETNAME).click()
        return elem_basketname

    def find_elem_basketname(self, value):
        find_basketname = self.find_element(LocatorsProject.PCB_vBASKETNAMEIN).send_keys(value)
        return find_basketname

    def elem_click_basketlastname(self):
        elem_basketlastname = self.find_element(LocatorsProject.PCB_fBASKETLASTNAME).click()
        return elem_basketlastname

    def find_elem_basketlastname(self, value):
        find_basketlastname = self.find_element(LocatorsProject.PCB_vBASKETLASTNAMEIN).send_keys(value)
        return find_basketlastname

    def btn_click_basketpickup(self):
        btn_basketpickup = self.find_element(LocatorsProject.PCB_bBASKETPICKUP)
        return btn_basketpickup

    def btn_click_basketpickup1(self):
        btn_basketpickup1 = self.find_element(LocatorsProject.PCB_bBASKETPICKUP1).click()
        return btn_basketpickup1

    def btn_click_basketpickuphere(self):
        btn_basketpickuphere = self.find_elements(LocatorsProject.PCB_bBASKETPICKUPHERE)[0].click()  # +S
        return btn_basketpickuphere

    def btn_click_basketpayment(self):
        btn_basketpayment = self.find_element(LocatorsProject.PCB_bBASKETPAYMENT)
        return btn_basketpayment

    def btn_click_basketpay(self):
        btn_basketpay = self.find_element(LocatorsProject.PCB_bBASKETPAY)
        return btn_basketpay

    def find_elem_basketorderok(self):
        find_basketorderok = self.find_element(LocatorsProject.PCB_fBASKETORDEROK)
        return find_basketorderok

    def find_elem_numbergoods(self):
        find_numbergoods = self.find_element(LocatorsProject.PCB_fNUMBERSGOODS)
        return find_numbergoods
