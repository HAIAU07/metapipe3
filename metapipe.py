import tkinter as tk
from tkinter import messagebox

import re
import os
import sys
if getattr(sys, 'frozen', False):
    # Running in a bundle (PyInstaller)
    source_folder = os.path.dirname(sys.executable)
else:
    # Running in a normal Python environment
    source_folder = os.path.dirname(os.path.abspath(__file__))
source_folder_icons = os.path.join(source_folder, "maya2024/Icons")

MetapipeEULA = """Metapipe Tool \n\nEnd User Licence Agreement \n\n\n\nThis End User Agreement applies to all downloadable products including 'Metapipe Character Customization and Rigging Tool' and professional services (e.g. \n\n3D models, tutorials, mentorships, personal training) sold via the Arts and Spells or Artstation Marketplace. \n\nAll rights and copyrights of the Metapipe Tool mentioned in this agreement belong to Arts and Spells Software Technologies Incorporate Company (Arts and Spells Yaz'l'm Teknolojileri A.'., as original legal name). \n\nIn this contract; Arts and Spells Software Technologies Incorporate Company is the licensee, creator and holder of all rights of the Metapipe product/tool. \n\n\n\nThe EULA is an agreement between the buyer and the seller (Arts and Spells Software Technologies Incorporate Company) providing the goods or services. \n\n\n\n\n\nPLEASE READ THIS DOCUMENT CAREFULLY. \n\nIT SIGNIFICANTLY ALTERS YOUR LEGAL RIGHTS AND REMEDIES. \n\nBY CLICKING 'I AGREE' OR DOWNLOADING OR USING THE DIGITAL PRODUCT OR RECEIVING THE PROFESSIONAL SERVICES TO WHICH THIS AGREEMENT RELATES YOU ACCEPT ALL OF THIS AGREEMENT'S TERMS, INCLUDING THE DISCLAIMERS OF WARRANTIES AND LIMITATIONS ON DAMAGES, USE AND TRANSFERABILITY. \n\nIF YOU DO NOT ACCEPT THIS AGREEMENT'S TERMS, DO NOT DOWNLOAD, INSTALL OR USE THE DIGITAL PRODUCT OR RECEIVE OR USE THE PROFESSIONAL SERVICES. \n\n\n\n\n\nThis end-user agreement ('Agreement') is a legally binding agreement between you, the licensee and customer ('you' or 'your'), and the provider ('we' or 'us' or 'our') of the digital products ('Products') or instructional, training, mentorship or other professional service packages ('Professional Services') that you purchase Metapipe Character Customization and Rigging Tool through the ArtStation or Arts and Spells Marketplace, regarding your rights and obligations regarding those Products and Professional Services. \n\n \n\n\n\n1. Your Legal Status \n\n\n\nIn this Agreement, 'you' means the person or entity acquiring rights in the Products or purchasing Professional Services. \n\nThat may be a natural person, or a corporate or business entity or organization. \n\nThis agreement is made between you and Arts and Spells Software Technologies Incorporate Company and is legally binding. \n\n\n\n(a) If you are a natural person then you must be, and you confirm that you are, at least 13 years old. \n\nIf you are between 13 years and the age of majority in your jurisdiction of residence, you confirm that your parent or legal guardian has reviewed and agrees to this Agreement and is happy for you to access and use the Product or receive the Professional Services. \n\n\n\n\n\n(b) If you are a corporate entity then: (i) the rights granted under this Agreement are granted to that entity; (ii) you represent and warrant that the individual completing and accepting this Agreement is an authorized your representative and has the authority to legally bind that you to the Agreement; and (iii) to the extent that one or more of your employees are granted any rights in the Product or to receive Professional Services under this Agreement, you will ensure that your employees comply with this Agreement and you will be responsible and liable for any breach of this Agreement by any employee. \n\n\n\n\n\n2. What's Metapipe? \n\n\n\n(a) Metapipe is a character customization and rigging tool works together with Epic Game's Metahuman System, developed by Arts and Spells Software Technologies Incorporate Company. \n\n \n\n\n\n(b) You acknowledge and agree that Epic is a third-party beneficiary of this Agreement and therefore will be entitled to directly enforce and rely upon any provision in this Agreement that confers a benefit on, or rights in favour of, Epic. \n\nIn addition, you authorize Epic to act as your authorized representative to file a lawsuit or other formal action against a licensor in a court or with any other governmental authority if Epic knows or suspects that a licensor breached any representations or warranties under this Agreement. \n\nThe foregoing authorization is nonexclusive, and Epic shall be under no obligation to pursue any claim. \n\nEpic will not initiate any such action on your behalf without first consulting with and obtaining your approval. \n\nYou can read and be informed about Epic Games' privacy policy here https://www.epicgames.com/privacypolicy \n\n\n\n3. Product Licence \n\n\n\n(a) Subject to this Agreement's terms and conditions, we hereby grant you a limited, non-exclusive, worldwide, non-transferable right and licence to (which will be perpetual unless the licence terminates as set out in this Agreement): (a) download the Product; and (b) copy and use the Product. \n\nWe reserve all rights not expressly granted to you under this Agreement. \n\n \n\n\n\n(b) Metapipe reserves the rights regarding malicious use of the license. \n\n\n\n\n\n(c) The Metapipe user, will be responsible for the working principles, copyrights and user agreements of the partnered companies in joint work and development with other companies for the improvement of the Tool or for other reasons. \n\n\n\n\n\n4. Licence Scope and Restrictions \n\n\n\n(a) Licence Usage \n\n\n\nYou are purchasing ONE licence to create ONE copy of the Product for use by you only (or, if you are a corporate entity, for use by a single authorized employee). \n\nIf it is a company that employs more than two workers or has an annual turnover of more than 100,000 USD, it must obtain a commercial Company license. \n\nCompanies mentioned in this article (with at least two employees and an annual turnover of over 100,000 USD) cannot purchase a retail license, even for trial purposes. \n\nFor this, they must use a trial license. \n\n\n\n\n\n(b) Refund \n\n\n\nIn the case described above, if it is determined that a company has obtained a personal license, the parties either agree within 14 days to switch to commercial use with an appropriate price increase and payment of compensation, or the license is terminated unilaterally by Arts and Spells, without prejudice to compensation and commercial rights. \n\nIn this case, Arts and Spells will not provide any refund. \n\n\n\n\n\nIn commercial purchases, the logo and name of the purchasing company may be displayed in Metapipe's visuals, on the website, in various images, videos and in areas showing its portfolio. \n\nBy signing this contract, the purchasing company accepts this in commercial purchases. \n\n\n\n\n\nIf this Product is bundled with a stock digital asset, then you receive a limited personal use licence regarding that stock digital asset, and you may use that stock digital asset for your personal use only. \n\nYou will not use that stock digital asset in any commercial manner unless you purchase a separate commercial licence. \n\nFree versions may never be used for commercial purposes. \n\n\n\n\n\nIf an effective feature does not work to fulfill its purpose during the use of the Tool, and if the user's problem is not resolved within 1 week despite the necessary feedback being given to Arts and Spells Team on Discord Support, a refund can be made. \n\nOther than this, no refund will be given under any circumstances. \n\n\n\n\n\n(d) Installable Tools \n\n\n\nYou may purchase one or more licences for the Product. \n\nA single licence allows you to install the Product on a single computer at a time for use by a single authorized user. \n\nIf you are a corporate entity and the authorized employee completing the transaction on your behalf purchases multiple licences, you may choose to store the Product on a single server or shared hard drive for use by a single authorized employee at a time for each licence purchased. \n\nHowever, as stated in the rest of the agreement, a single license can only be used by one employee and malicious use is prevented. \n\n\n\n\n\nProvided that you comply with the restrictions on users set out above, you may use the Product on an unlimited number of projects. \n\n\n\n\n\nMetapipe will not guarantee the performance and service of trial and trial versions, or support during and after use. \n\nThere are differences between the purchased versions of the Tool and the free versions. \n\n\n\n\n\n(e) Stock Assets \n\n\n\nSubject to the restrictions set out in this Agreement, you may copy, use, modify, adapt, translate, publicly display, transmit, broadcast, and create derivative works from the Product in works you create ('Works'), which may include things like films, videos, multi-media projects, computer games, models, images, publications, broadcasts, documents, and presentations. \n\n\n\n\n\nThe sale of MetaHumans, their commercial use, and similar misuse through the Metapipe tool is strictly prohibited. \n\nIf such a situation is detected, the user will be banned indefinitely by support. \n\nThe use of MetaHumans can only be used in the user's own projects and works. \n\n\n\n\n\nIf you are a corporate entity, you may make the Product available for use by your employees in accordance with this Agreement (for example, by storing the Product on a network server). \n\n\n\n\n\nYou may only share the Product with external people or entities where: \n\n\n\nYou are collaborating with the external parties in the creation of your Work and you need to share the Product for that purpose, provided that any external party that receives the Product may only use it in your Work and must secure and limit access to the Product for that purpose; \n\nYou are working as a contractor for a client in the creation of a Work and need to share the Product with your client, or any external parties working with your client, provided that your client and any such external parties may use the Product only for your client's Work, and all parties secure and limit access to the Product for that purpose. \n\n\n\n\n\nFor any other use of the Product by any other party, that party must purchase a licence to the Product. \n\n\n\n\n\nIn addition to any other restrictions in this Agreement, you will not: \n\npublish, sell, license, offer or make available for sale or licensing, or otherwise distribute the Product except as part of a Work or through a form of sharing that is authorized in this Agreement; or \n\npublish, distribute or make available the Product through any online clearinghouse platform. \n\n\n\n\n\n5. How Does Metapipe Work? What Does It Offer You? \n\n\n\n(a) Metapipe; application/tool works together with the product called MetaHuman, whose patent and usage rights belong to Epic Games. \n\nUsers can make changes to their MetaHumans through the tool by using Epic Game's DNA Calibration codes and automated rigging algorithms of Metapipe inside and outside of Autodesk Maya. \n\nThese changes are made and used by the user of the application; It is entirely the responsibility of the user in terms of the terms of use, user agreement and other legal terms determined by Epic Games, Metahuman EULA and DNA Calibration License Agreement. \n\n\n\n\n\n(b) Metapipe and the services and products it provides; It has no responsibility for the development of MetaHumans or for decisions that may be taken unilaterally by Epic games. \n\nNamely; The application offered by Metapipe allows customization of MetaHuman owned only by the Metahuman user. \n\nApart from this, Metapipe is not responsible in cases where MetaHumans become paid for in the future, are completely eliminated, or are made to fundamental changes. \n\nIn such a case, the user will not be able to request a refund or other compensation from Metapipe. \n\n\n\n\n\nMetapipe will be able to collaborate commercially with other companies or individuals, including the development of the tool. \n\nIn this sense, Metapipe and Arts and Spells reserve the right to make positive or negative changes that may occur in the general features of the tool. \n\nThis does not give the user the right to claim compensation or refund. \n\nIn contracts made with such third parties and companies to which Arts and Spells and Metapipe are parties, users must comply with the user notifications, manifestos and rules of the other party. \n\n\n\n\n\n(c) The limits of what the service and application provided by Metapipe can do are within the limits set by Epic Games. \n\nThe application may not be capable of providing any changes beyond these limits and this cannot be guaranteed by Metapipe. \n\nUsers are responsible for complying with MetaHuman and DNA Calibration rules. \n\nThe rules specified in the MetaHuman and DNA Calibration user agreements are fully binding on the users. \n\nThe user will be responsible if the service and application provided by Metapipe is used outside of these rules and agreements. \n\n\n\n\n\n(d) If there is a change in Epic Games' license terms or if the application violates these license terms, Metapipe may unilaterally make changes to the application. \n\nRestrictions to be applied by Epic Games, fundamental changes and changes to the application in matters that Metapipe must strictly comply with will be considered mandatory. \n\nMetapipe is not responsible for any damages or data loss resulting from these changes. \n\nThese apply in all cases that affect product features, including when advertised features become unavailable during the marketing of the product, when Epic Games prohibits or prevents the use of third-party software. \n\nMetapipe is not liable for any compensation in such a case. \n\n\n\n\n\n(e) 3D Models, Topologies, Character Templates and any other related products or designs made and sold seperately by Arts and Spells are not MetaHuman. \n\nHowever, they can transform into MetaHuman by using only Metapipe. \n\n\n\n\n\n(f) Metapipe is not responsible for any problems that the user (commercial or individual) may encounter due to computer hardware while using the tool. \n\nEach user is responsible for the hardware that will enable the tool to operate efficiently. \n\n\n\n\n\n6. Additional Restrictions \n\n\n\nExcept as expressly permitted under this Agreement, you will not: \n\n\n\n(a) make any copy of the Product except for archival or backup purposes; \n\n\n\n(b) circumvent or disable any access control technology, security device, procedure, protocol, or technological protection mechanism that may be included or established in or as part of the Product; \n\n\n\n(c) hack, reverse engineer, decompile, disassemble, modify or create derivative works of the Product or any part of the Product; \n\n\n\n(d) publish, sell distribute or otherwise make the Product available to others to use, download or copy; \n\n\n\n(e) transfer or sub-license the Product or any rights under this Agreement to any third party, whether voluntarily or by operation of law; \n\n\n\n(f) use the Product for any purpose that may be defamatory, threatening, abusive, harmful or invasive of anyone's privacy, or that may otherwise violate any law or give rise to civil or other liability; \n\n\n\n(g) misrepresent yourself as the creator or owner of the Metapipe; \n\n\n\n(h) remove or modify any proprietary notice, symbol or label in or on the Product; \n\n\n\n(i) directly or indirectly assist, facilitate or encourage any third party to carry on any activity prohibited by this Agreement. \n\n\n\n\n\n(j) 3D Models, designs, intellectual products and topologies (the points, lines and surfaces that make up the model) made by Arts and Spells belong entirely to Arts and Spells. \n\nThese can be used within the Tool, but cannot be sold, shared or copied in any way for commercial purposes. \n\n\n\n\n\n(k) This License Agreement does not grant you any right, title or interest in the trademarks, service marks, trade names, and logos associated with Epic, Epic's games and other intellectual property, including Metapipe. \n\n\n\n\n\n(l) One purchased license can only be used on one computer. \n\nIt is not possible to switch from one computer to another while using the license. \n\nAlthough the user has the right to reset the license, Arts and Spells decides whether this is appropriate or not. \n\nIf the user has a valid reason, notifies Arts and Spells. \n\nResetting too frequently or similar actions are considered malicious. \n\n\n\n\n\n7. Proprietary Rights \n\n\n\nThe Product is protected by copyright laws and international copyright treaties, as well as other intellectual property laws and treaties. \n\nYou are licensing the Product and the right to access, install and use the Product in accordance with this Agreement, not buying the Product and its copyrights. \n\nAs between you and us, we own all right, title and interest in and to the Product, and you are not acquiring any ownership of or rights in the Product except the limited rights granted under this Agreement. \n\n\n\n\n\n8. No Epic Support \n\n\n\nYou acknowledge and agree that you are licensing the Product from us (the Provider), not from Epic, and that Epic has no obligation to support the Product. \n\nMetapipe does not have any maintenance or support obligations with respect to MetaHuman Technology, nor does Metapipe have any obligation to continue to make MetaHuman Technology available for access or use. \n\n\n\n\n\n9. Interruptions and Errors \n\nYour use of the Product might be interrupted and might not be free of errors. \n\nMetapipe cannot guarantee you this under any circumstances. \n\nSuch interruptions or problems may also be caused by Epic or MetaHuman. \n\n\n\n\n\n10. Updates \n\nWe have no obligation to update the Product. \n\n\n\n\n\n11. Provision of Professional Services \n\n\n\n(a) We will provide the Professional Services directly to you and, subject to this Agreement, will assume all responsibility for all aspects of the Professional Services. \n\nWe represent and warrant that we have the right to offer and provide the Professional Services and that we have appropriate qualifications and experience to provide the Professional Services. \n\n\n\n\n\n(b) General use and effective use of the Tool by the user may occur within a certain period. \n\nA reason such as the program cannot be used for this reason cannot be considered reasonable. \n\nThis period may vary from user to user. \n\n\n\n\n\nIt may take some time to adapt to the use of Metapipe and its tools, menu dynamics and the working principles of the program. \n\nThis time may vary depending on the user's own abilities, hardware and computer he uses, and the time spend with program. \n\n\n\n\n\n12. Support \n\n\n\n(a) There is a Discord support service, but Arts and Spells is not obliged to provide this service under all circumstances. \n\nIn future applications, this service may be terminated completely. \n\nArts and Spells is not responsible for any opinions or other facts reported to Support. \n\nSince there is no confidentiality agreement between the parties, no legal liability will arise for the parties in similar or identical situations. \n\n\n\n\n\n(b) In cases of non-compliance with server rules or Epic's user agreement, support may ban the user. \n\nIn this case, support does not have to be given. \n\n\n\n\n\n13. Epic is not Involved \n\n\n\nYou acknowledge and agree that: \n\n\n\n(a) this Agreement (and any dispute under it) is an agreement between us and you only, and not with Epic, and Epic is not a party to this Agreement; \n\n\n\n(b) we are not Epic's employee, agent or subcontractor; \n\n\n\n(c) Epic does not have any obligation to attempt to resolve any dispute between us and you; and \n\n\n\n(e) we will provide the Professional Services directly to you, and we (and not Epic) are solely responsible for the Professional Services, and Epic has no obligation or liability to you with respect to the Professional Services. \n\n\n\n\n\n14. Disclaimer \n\n\n\nANY PRODUCTS OR PROFESSIONAL SERVICES ARE PROVIDED ON AN 'AS IS' AND 'AS AVAILABLE' BASIS, WITHOUT ANY REPRESENTATIONS, WARRANTIES OR CONDITIONS OF ANY KIND. \n\n\n\n\n\nNEITHER WE/ARTS AND SPELLS SOFTWARE TECHNOLOGIES INCORPORATE COMPANY/Metapipe NOR ANY OF THE METAHUMAN PARTIES REPRESENT OR WARRANT THAT: (A) ANY PRODUCT OR PROFESSIONAL SERVICE IS ACCURATE, COMPLETE, RELIABLE, CURRENT OR ERROR-FREE; (B) ANY PRODUCT OR PROFESSIONAL SERVICE WILL MEET YOUR REQUIREMENTS OR EXPECTATIONS; (C) ANY DEFECTS IN ANY PRODUCT OR PROFESSIONAL SERVICE WILL BE CORRECTED. \n\n\n\n\n\n15. Exclusion and Limitation of Liability \n\n\n\n(a) YOU DOWNLOAD, INSTALL AND OTHERWISE USE ALL PRODUCTS, AND RECEIVE AND USE ALL PROFESSIONAL SERVICES, AT YOUR OWN RISK. \n\nYOU AGREE TO, AND HEREBY DO: \n\n\n\nWAIVE ANY CLAIMS THAT YOU MAY HAVE AGAINST ARTS AND SPELLS SOFTWARE TECHNOLOGIES JOINT STOCK COMPANIES/Metapipe OR THE EPIC PARTIES OR OUR RESPECTIVE DIRECTORS, OFFICERS, EMPLOYEES, AGENTS, REPRESENTATIVES, LICENSORS, SUCCESSORS AND ASSIGNS (COLLECTIVELY THE 'RELEASEES') ARISING FROM OR RELATING TO ANY PRODUCTS OR PROFESSIONAL SERVICES, AND \n\n\n\nRELEASE THE RELEASEES FROM ANY LIABILITY FOR ANY LOSS, DAMAGE, EXPENSE OR INJURY ARISING FROM OR RELATING TO YOUR USE OF ANY PRODUCT OR PROFESSIONAL SERVICE, WHETHER ARISING IN TORT (INCLUDING NEGLIGENCE), CONTRACT OR OTHERWISE, EVEN IF THE RELEASEES ARE EXPRESSLY ADVISED OF THE POSSIBILITY OF SUCH LOSS, INJURY OR DAMAGE AND EVEN IF THAT LOSS, INJURY OR DAMAGE IS FORESEEABLE. \n\n\n\n\n\n(b) NEITHER WE; ARTS AND SPELLS SOFTWARE TECHNOLOGIES INCORPORATE COMPANY/Metapipe NOR THE EPIC PARTIES WILL BE LIABLE FOR ANY LOSSES, DAMAGES, CLAIMS OR EXPENSES THAT CONSTITUTE: (I) LOSS OF INTEREST, PROFIT, BUSINESS, CUSTOMERS OR REVENUE; (II) BUSINESS INTERRUPTIONS; (III) COST OF REPLACEMENT PRODUCTS OR SERVICES; OR (IV) LOSS OF OR DAMAGE TO REPUTATION OR GOODWILL. \n\n\n\n\n\n(c) NEITHER WE; ARTS AND SPELLS SOFTWARE TECHNOLOGIES INCORPORATE COMPANY/ Metapipe NOR THE EPIC PARTIES WILL BE LIABLE FOR ANY LOSSES, DAMAGES, CLAIMS OR EXPENSES THAT CONSTITUTE INCIDENTAL, CONSEQUENTIAL, SPECIAL, PUNITIVE, EXEMPLARY, MULTIPLE OR INDIRECT DAMAGES, EVEN IF WE HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH LOSSES, DAMAGES, CLAIMS OR EXPENSES. \n\n\n\n\n\n(d) MAXIMUM LIABILITY: SINCE ARTS AND SPELLS SOFTWARE TECHNOLOGIES INCORPORATE COMPANY/Metapipe IS NOT A DIRECT SERVICE PROVIDER OF METAHUMAN, IT DOES NOT HAVE ANY RESPONSIBILITY IN THIS SENSE. \n\n \n\n\n\n16. Indemnity \n\n\n\nAs a condition of your use of any Product or any Professional Services, you agree to hold harmless and indemnify the Releasees from any liability for any loss or damage to any third party resulting from your access to, installation or use of the Product or your receipt and use of the Professional Services. \n\n\n\n\n\n17. Term and Termination \n\n\n\nThis agreement is valid until termination by the parties or until the end of the license period. \n\nMetapipe reserves the right to terminate immediately in case of abusive use. \n\nYour rights under this Agreement will terminate automatically without notice if: (a) you breach any terms of this Agreement; or (b) you do not complete payment for the Product or Professional Services, or any payment you make is refunded, reversed or cancelled for any reason. \n\nUpon this Agreement's termination, you will cease all use of the Product and destroy all copies, full or partial, of the Product in your possession. \n\n \n\n\n\n18. Compliance with Laws \n\n\n\nYou will comply with all applicable laws when using any Product or Professional Services (including intellectual property and export control laws). \n\n\n\n\n\n19. Entire Agreement \n\n\n\nThis Agreement supersedes all prior agreements of the parties regarding the Product or Professional Services, and constitutes the whole agreement with respect to the Product or Professional Services. \n\nMetapipe has the right to make unilateral changes to the contract articles. \n\n\n\n\n\n20. Disputes \n\n\n\nIf you have any concerns about the Product or Professional Services, please contact us through our Metapipe Marketplace account and we will work with you to try to resolve the issue. \n\nYou acknowledge and agree that any such dispute is between you and us, and that Epic will not be involved in the dispute and has no obligation to try to resolve the dispute. \n\n\n\n\n\n21. Persons Bound \n\n\n\nThis Agreement will enure to the benefit of and be binding upon the parties and their heirs, executors, administrators, legal representatives, lawful successors and permitted assigns. \n\n\n\n\n\n22. Assignment \n\n\n\nWe may assign this Agreement without notice to you. \n\nWe also have the right to transfer Metapipe materials and our contractual responsibilities on a commercial basis. \n\n\n\n\n\nYou may not assign this Agreement or any of your rights under it without our prior written consent, which we will not withhold unreasonably. \n\n\n\n\n\n23. Waiver \n\n\n\nNo waiver, delay, or failure to act by us regarding any particular default or omission will prejudice or impair any of our rights or remedies regarding that or any subsequent default or omission that are not expressly waived in writing. \n\n\n\n\n\n24. Applicable Law and Jurisdiction \n\n\n\nSince Arts and Spells is located in Turkey, this agreement is governed by the laws of Turkey. Apart from this, you are also responsible in terms of local and international law and you acknowledge this. \n\n\n\n25. Severability. \n\n\n\nIf any provision of this Agreement shall be held or made invalid by a court decision, statute or rule, or shall be otherwise rendered invalid, the remainder of this Agreement shall not be affected thereby.\n\n\n\n26. Legal Effect \n\n\n\nThis Agreement describes certain legal rights. \n\nYou may have other rights under the laws of your country. \n\nThis Agreement does not change your rights under the laws of your country if the laws of your country do not permit it to do so. \n\n\n\n\n\n27. Interpretation \n\n\n\nIn this Agreement, "we", "us", and "our" refer to the licensor of the Product alone and never refer to the combination of you and that licensor (that combination is referred to as "the parties"), or the combination of you or the licensor with Epic. \n\n\n\n\n28. Miscellaneous \n\n\n\nThis Agreement constitutes the entire agreement between you and Arts and Spells relating to the subject matter covered by this Agreement. \n\nAll other communications, proposals, and representations with respect to the subject matter covered by this Agreement are excluded. \n\n\n\n\n\nThe original of this Agreement is in English; any translations are provided for reference purposes only. \n\nYou waive any right you may have under the law of your country to have this Agreement written or construed in the language of any other country. \n\n\n\n\n\nThis Agreement describes certain legal rights. \n\nYou may have other rights under the laws of your jurisdiction. \n\nThis Agreement does not change your rights under the laws of your jurisdiction if the laws of your jurisdiction do not permit it to do so. \n\nLimitations and exclusions of warranties and remedies in this Agreement may not apply to you because your jurisdiction may not allow them in your particular circumstance. \n\nIn the event that certain provisions of this Agreement are held by a court or tribunal of competent jurisdiction to be unenforceable, those provisions shall be enforced only to the furthest extent possible under applicable law and the remaining terms of this Agreement will remain in full force and effect. \n\n\n\n\n\nAny act by Metapipe to exercise, or failure or delay in exercise of, any of its rights under this Agreement, at law or in equity will not be deemed a waiver of those or any other rights or remedies available in contract, at law or in equity. \n\n\n\n\n\nYou agree that this Agreement does not confer any rights or remedies on any person other than the parties to this Agreement, except as expressly stated. \n\n\n\nMetapipe's obligations are subject to existing laws and legal process, and Metapipe may comply with law enforcement or regulatory requests or requirements despite any contrary term in this Agreement."""


mtpHeader = "\nMETAPIPE EULA\n\n"

def install_metapipe_free():
    from metapipeFree import freeInstaller
    freeInstaller.run()
    btn_metapipe_free.config(state=tk.NORMAL, text="Metapipe Free is installed!", bg="#444444")
    btn_metapipe.config(state=tk.NORMAL, text="Install Metapipe", command=install_metapipe, bg="green", fg="white", width=widthBut, font=button_font)
    print("Metapipe Free installed.")

file_path = "c:/Arts and Spells/Scripts/dat.py"
MAIN = "C:/Arts and Spells/Metapipe Studio 3.0.0"
 
def metapipe():
    from maya2024 import studioInstaller24
    studioInstaller24.run()

    # Open the file in read mode
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()

        # Use a regular expression to replace MAIN_PATH assignment
        pattern = re.compile(r'MAIN_PATH\s*=\s*"[^"]+"')
        content = pattern.sub('MAIN_PATH = "' + MAIN + '"', content)

        # Open the file in write mode and save the modified content
        with open(file_path, 'w') as file:
            file.write(content)

        print("Variable MAIN_PATH updated successfully.")

    btn_metapipe.config(state=tk.NORMAL, text="Metapipe is installed succesfully!", command=install_metapipe, bg="green", fg="white", width=widthBut, font=button_font)


def show_metapipeEULA(root):
    license_window = tk.Toplevel(root)
    license_window.title("Metapipe EULA")
    license_window.geometry("600x600")
    license_window.resizable(False, False)

    # Create a frame for the text and scrollbar
    text_frame = tk.Frame(license_window)
    text_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Create a scrollbar
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a text widget with the license text
    license_text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    license_text.tag_configure("title", font=("Helvetica", 16, "bold"))
    # Insert the title with the defined style
    license_text.insert(tk.END, mtpHeader, "title")
    license_text.insert(tk.END, MetapipeEULA)
    license_text.config(state=tk.DISABLED)  # Make the text read-only
    license_text.pack(expand=True, fill=tk.BOTH)

    # Configure the scrollbar to scroll the text widget
    scrollbar.config(command=license_text.yview)

    # Create a frame for the checkbox and button
    action_frame = tk.Frame(license_window)
    action_frame.pack(pady=10)

    agree_var = tk.IntVar()

    # Function to enable the Next button
    def enable_next_button():
        if agree_var.get() == 1:
            next_button.config(state=tk.NORMAL)
        else:
            next_button.config(state=tk.DISABLED)

    # Create the checkbox
    agree_check = tk.Checkbutton(action_frame, text="I agree to the terms and conditions", variable=agree_var, command=enable_next_button)
    agree_check.pack(side=tk.LEFT)

    # Create the Next button
    next_button = tk.Button(action_frame, text="Install", state=tk.DISABLED, command=lambda: [license_window.destroy(), metapipe()])
    next_button.pack(side=tk.LEFT, padx=10)

def install_metapipe():
    show_metapipeEULA(root)
    
    

# Create the main window
root = tk.Tk()
root.title("Metapipe Installation")
root.geometry("300x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Load and display the logo image
logo_path = source_folder_icons + "/Metapipe3Icon.png"
logo_img = tk.PhotoImage(file=logo_path)

logo_label = tk.Label(root, image=logo_img, bg="#1e1e1e")
logo_label.pack(pady=30)

installation_label = tk.Label(root, text="INSTALLATION", font=("Helvetica", 16, "bold"), bg="#1e1e1e", fg="white")
installation_label.pack(pady=0)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=20)

button_font = ("Segoe UI", 10, "bold")
widthBut = 25
heightBut = 2
# Create a StringVar to hold the input text
user_input_var = tk.StringVar()

# Create a label for the text field
input_label = tk.Label(root, text="Enter License Key:", font=("Helvetica", 10), bg="#1e1e1e", fg="white")
input_label.pack(pady=(10, 5))

# Create the text field (Entry widget)
input_entry = tk.Entry(root, textvariable=user_input_var, width=30)
input_entry.pack(pady=5)

# Function to handle the button click
def show_lic_messagebox():
    custom_messagebox = tk.Toplevel()
    custom_messagebox.title("Message")
    custom_messagebox.resizable(False, False)
    custom_messagebox.configure(bg="#1e1e1e")

    message = tk.Label(custom_messagebox, text="Invalid License Structure. Please check your license structure. Example: SCAFA1-8477DB-428996-5B0255-6D5F0D-3C1FCF", padx=20, pady=20,bg="#1e1e1e", fg = "white")
    message.pack()

    button_frame = tk.Frame(custom_messagebox,bg="#1e1e1e")
    button_frame.pack(pady=10)

    ok_button = tk.Button(button_frame, text="Okay", command=lambda: custom_messagebox.destroy(), width=12,bg="#1e1e1e", fg = "white")
    ok_button.pack(side=tk.LEFT, padx=5)

    #tutorial_button = tk.Button(button_frame, text="Watch Tutorial", command=lambda: open_tutorial("https://youtu.be/A8a0DcdduEQ"), width=12, bg="green", fg = "white")
    #tutorial_button.pack(side=tk.LEFT, padx=5)

def update_variable():
    user_input = user_input_var.get()
    user_input = user_input.replace("'","")
    user_input = user_input.replace('"',"")
    if not len(user_input) == 41:
        show_lic_messagebox()
    else:
        os.makedirs(MAIN, exist_ok=True)
        output_file_path = MAIN + '/MetapipeLIC.py'
        # Read the contents of ps.py
        with open(output_file_path, 'w') as output_file:
            output_file.write('LicenseKey = "' + user_input + '"')
        print("User input:", user_input)
    # You can use user_input as a variable anywhere
    # For example, pass it to metapipe():
    # metapipe(user_input)

# Create the update button
update_button = tk.Button(root, text="Update License", command=update_variable, bg="green", fg="white", font=button_font)
update_button.pack(pady=10)
# Create buttons with dark theme
btn_metapipe_free = tk.Button(button_frame, text="Install Metapipe Free", command=install_metapipe_free, bg="green", fg="white", width=widthBut, font=button_font, height=heightBut)
btn_metapipe = tk.Button(button_frame, text="Install Metapipe", command=install_metapipe, bg="green", fg="white", width=widthBut, font=button_font, height=heightBut)

installation_label2 = tk.Label(root, text="Arts and Spells Inc.", font=("Helvetica", 9, "bold"), bg="#1e1e1e", fg="white")
installation_label2.pack(pady=0)
#btn_shelf = tk.Button(button_frame, text="Shelf Tutorial", command=install_metapipe, bg="#444444", fg="white", width=15, font=button_font)
if not os.path.exists('C:/Arts and Spells/Metapipe Free 3.0.0'):
    btn_metapipe.config(state=tk.DISABLED, text="Install the Free Version First!", bg="#444444")
else:
    btn_metapipe_free.config(state=tk.NORMAL, text="Metapipe Free is installed!", bg="#444444")

# Place buttons on the window
btn_metapipe_free.pack(pady=10)
btn_metapipe.pack(pady=10)
#btn_shelf.pack(pady=10)

root.mainloop()