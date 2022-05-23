import os
import openai
openai.api_key = '' #your api key goes here

input = """
Context: Isotopes are different forms of an element that have the same number of protons but a different number of neutrons. Some elements—such as carbon, potassium, and uranium—have naturally occurring isotopes. Carbon-12 contains six protons, six neutrons, and six electrons; therefore, it has a mass number of 12 (six protons and six neutrons). Carbon-14 contains six protons, eight neutrons, and six electrons; its atomic mass is 14 (six protons and eight neutrons). These two alternate forms of carbon are isotopes.

Target: neutrons

Question: How many neutrons do carbon-12 and carbon-13 have, respectively?

Answer: Carbon-12 contains  6  neutrons while carbon-13 contains  7  neutrons.

###

Context: Ionic and covalent bonds between elements require energy to break. Ionic bonds are not as strong as covalent, which determines their behavior in biological systems. However, not all bonds are ionic or covalent bonds. Weaker bonds can also form between molecules. Two weak bonds that occur frequently are hydrogen bonds and van der Waals interactions. Without these two types of bonds, life as we know it would not exist. Hydrogen bonds provide many of the critical, life-sustaining properties of water and also stabilize the structures of proteins and DNA, the building block of cells.

Target: Hydrogen bonds

Question: Why are hydrogen bonds and van der Waals interactions necessary for cells?

Answer: Hydrogen bonds and van der Waals interactions form weak associations between and/or within molecules, providing the necessary shape and structure of DNA and proteins to function in the body.

###

Context: Atoms of each element contain a characteristic number of protons and electrons. The number of protons determines an element’s atomic number, which scientists use to distinguish one element from another. The number of neutrons is variable, resulting in isotopes, which are different forms of the same atom that vary only in the number of neutrons they possess. Together, the number of protons and neutrons determine an element’s mass number, as Figure 2.3 illustrates. Note that we disregard the small contribution of mass from electrons in calculating the mass number. We can use this approximation of mass to easily calculate how many neutrons an element has by simply subtracting the number of protons from the mass number.

Target: neutrons

Question: If xenon has an atomic number of  54  and a mass number of  108 , how many neutrons does it have?

Answer: 54, since the mass number minus the atomic number is 54.

###

Context: One of water’s important properties is that it is composed of polar molecules: the hydrogen and oxygen within water molecules (H2O) form polar covalent bonds. While there is no net charge to a water molecule, water's polarity creates a slightly positive charge on hydrogen and a slightly negative charge on oxygen, contributing to water’s properties of attraction. Water generates charges because oxygen is more electronegative than hydrogen, making it more likely that a shared electron would be near the oxygen nucleus than the hydrogen nucleus, thus generating the partial negative charge near the oxygen.

Target: polar covalent bonds

Question: Explain why the bonds within a water molecule are described as polar covalent bonds.

Answer: Oxygen is more electronegative than hydrogen, generating a partial negative charge near the oxygen atoms.

###

Context: Common disaccharides include lactose, maltose, and sucrose (Figure 3.8). Lactose is a disaccharide consisting of the monomers glucose and galactose. It is naturally in milk. Maltose, or malt sugar, is a disaccharide formed by a dehydration reaction between two glucose molecules. The most common disaccharide is sucrose, or table sugar, which is comprised of glucose and fructose monomers.

Target:  Lactose

Question: Which of these best describes the production of sucrose, maltose, and lactose?

Answer: Glucose and fructose combine to form sucrose. Glucose and galactose combine to form lactose. Two glucose monomers combine to form maltose.

###

Context: Prophase (the “first phase”): the nuclear envelope starts to dissociate into small vesicles, and the membranous organelles (such as the Golgi complex [Golgi apparatus] and the endoplasmic reticulum), fragment and disperse toward the periphery of the cell. The nucleolus disappears (disperses) as well, and the centrosomes begin to move to opposite poles of the cell. Microtubules that will form the mitotic spindle extend between the centrosomes, pushing them farther apart as the microtubule fibers lengthen. The sister chromatids begin to coil more tightly with the aid of condensin proteins and now become visible under a light microscope.

Target: condensin proteins
"""

response = openai.Completion.create(
    engine="davinci",
    prompt=input,
    max_tokens=200,
    top_p=1,
    n=50,
    temperature=0.9,
    echo=False,
    stop=["###","##","***","Context:"]
)

texts = []
for i in range(len(response.choices)):
    texts.append(response.choices[i].text)
    print(i,": ",response.choices[i].text)
